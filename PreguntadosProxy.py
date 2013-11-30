#!/usr/bin/env python
"""
This example builds on mitmproxy's base proxying infrastructure to
implement functionality similar to the "sticky cookies" option. This is at
a lower level than the Flow mechanism, so we're dealing directly with
request and response objects.
"""
from libmproxy import controller, proxy
import os
import re
from pprint import pprint

class PreguntadosMaster(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)
        self.stickyhosts = {}

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()
        
    def handle_response(self, msg):
        pprint (dir(msg))
        print "Content code dir: "
        pprint (dir(msg.content))
        print "Response code: %s" % msg.code 
        print "Response q: "
        pprint(dir(msg.q))
        print "Response content: %s" % msg.content
        print "Response headers: %s" % msg.headers
        


config = proxy.ProxyConfig(
    cacert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")
)
print "Launching Preguntados Cheater Proxy v0.1..."
server = proxy.ProxyServer(config, 8888)
m = PreguntadosMaster(server)
m.run()
print "Bye, bye cheater..."