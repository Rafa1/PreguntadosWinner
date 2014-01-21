#!/usr/bin/env python
"""
This example builds on mitmproxy's base proxying infrastructure to
implement functionality similar to the "sticky cookies" option. This is at
a lower level than the Flow mechanism, so we're dealing directly with
request and response objects.
"""
from libmproxy import controller, proxy
import libmproxy
import os
import re
from pprint import pprint
import json
from  colorama import Fore,Back

class PreguntadosMaster(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)
        self.stickyhosts = {}

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()
    """    
    def handle_request(self, msg):
        print "Estamos en handle_request"
        print "Tipo de msg es %s" % type(msg)
        print "Class de msg es %s" % msg.__class__
        print "Es el objeto msg de tipo flow.Request: %s" % isinstance(msg, libmproxy.flow.Request)
        print "Request es %s/%s" % (msg.get_url(),msg.get_query())
        dir(msg)
        # msg.send()
    """
    def handle_response(self, msg):
        #print "Tipo de msg es %s" % type(msg)
        #print "=== DIR(MSG) ====="
        #print dir(msg)
        # print "=================="
        # print "Class de msg es %s" % msg.__class__
        #print "msg.request.path es '%s'" % msg.request.path
        #print "msg.request.scheme es '%s'" % msg.request.scheme
        #print "msg.headers: "
        #print msg.headers
        #print "Encoding is: %s" % msg.headers["Content-Encoding"]

        content = msg.get_decoded_content()

        #print "msg.content: "
        #print content 
        if (msg.code == 200):
            if (re.match("\/api\/users\/\d+\/games\/\d+\/answers",msg.request.path) is not None):

                rjson = json.loads(content)
                normalq = rjson['spins_data']['spins'][0]['questions'][0]['question']
                powerupq = rjson['spins_data']['spins'][0]['questions'][0]['powerup_question']
    
                print "\n"
                print "=================="
                print "==== QUESTION ===="
                print "=================="
                print "%s " % (normalq['text'])
                # pprint(normalq)
                correcta_normal = int(normalq['correct_answer'])
                correcta_powerup = in(powerupq['correct_answer'])
                cont = 0
                for answer in normalq['answers']:
                    if cont == correcta_normal:
      #                  print colored("%s. %s" % (cont,answer),"green")
                        print (Fore.GREEN + "%s. %s" % (cont,answer))
                    else:
                        # print colored("%s. %s" % (cont,answer),"red")
                        print (Fore.RED + "%s. %s" % (cont,answer))
                    cont += 1
                print (Fore.RESET)
                print "==== POWERUP QUESTION ===="
                print "%s " % (powerupq['text'])
                # pprint(powerupq)
                cont = 0
                for answer in powerupq['answers']:
                    if cont == correcta_powerup:
      #                  print colored("%s. %s" % (cont,answer),"green")
                        print (Fore.GREEN + "%s. %s" % (cont,answer))
                    else:
                        # print colored("%s. %s" % (cont,answer),"red")
                        print (Fore.RED + "%s. %s" % (cont,answer))
                    cont += 1
                print (Fore.RESET)
        msg.reply()


config = proxy.ProxyConfig(
    cacert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")
)
print Fore.BLUE
print "  ********************************************"
print "  *   Author: Felipe Molina (@felmoltor)     *"
print "  *          Date: January 2014              *"
print "  *                                          *"
print "  *        PREGUNTADOS CHEATER v0.1          *"
print "  * Just showing you the correct answers :-) *"
print "  ********************************************"
print Fore.RESET
print "Proxy listening on 192.168.1.132:8888..."

server = proxy.ProxyServer(config, 8888)
m = PreguntadosMaster(server)
m.run()
print "Bye, bye cheater..."
