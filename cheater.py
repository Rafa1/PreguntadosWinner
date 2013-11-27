from pprint import pprint
import json
import re
from  colorama import Fore,Back

def response(context, flow):
    # print "Dir de context: "
    # pprint (dir(context))
    # print "Response msg: %s " % flow.response.msg
    if flow.response.code == 200:
        # print "Response request: "
        # pprint (dir(flow.response.request))
        # print "Path: %s" % flow.response.request.path
        if (re.match("\/api\/users\/\d+\/games\/\d+\/answers",flow.response.request.path) is not None):
     #       print "Response request path: %s " % flow.response.request.path
     #       print "Response content: "
            # Parseamos el JSON de la respuesta
            rjson = json.loads(flow.response.content)
            normalq = rjson['spins_data']['spins'][0]['questions'][0]['question']
            powerupq = rjson['spins_data']['spins'][0]['questions'][0]['powerup_question']

            print "\n"
            print "======================================"
            print "==== QUESTION ===="
            print "%s " % (normalq['text'])
            # pprint(normalq)
            correcta = int(normalq['correct_answer'])
            cont = 0
            for answer in normalq['answers']:
                if cont == correcta:
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
                if cont == correcta:
  #                  print colored("%s. %s" % (cont,answer),"green")
                    print (Fore.GREEN + "%s. %s" % (cont,answer))
                else:
                    # print colored("%s. %s" % (cont,answer),"red")
                    print (Fore.RED + "%s. %s" % (cont,answer))
                cont += 1
            print (Fore.RESET)

def request(context, flow):
    #pprint (vars(flow.request))
    #ppriint(vars(context))
    #print "=================="
    pass
