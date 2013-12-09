from pprint import pprint
import json
import re
from  colorama import Fore,Back

def response(context, flow):
    if flow.response.code == 200:
        # Open the output terminal as a file
        # ptsout = open("/dev/pts/3","w")
        
        if (re.match("\/api\/users\/\d+\/games\/\d+\/answers",flow.response.request.path) is not None):
            # Parseamos el JSON de la respuesta
            rjson = json.loads(flow.response.content)
            normalq = rjson['spins_data']['spins'][0]['questions'][0]['question']
            powerupq = rjson['spins_data']['spins'][0]['questions'][0]['powerup_question']
           
            print "\n"
            print "======================================"
            print "==== QUESTION ===="
            print "%s " % (normalq['text'])
            # ptsout.write("%s \n" % (normalq['text']))
            correcta = int(normalq['correct_answer'])
            cont = 0
            for answer in normalq['answers']:
                if cont == correcta:
                    print (Fore.GREEN + "%s. %s" % (cont,answer)) 
                else:
                    print (Fore.RED + "%s. %s" % (cont,answer))
                cont += 1
            print (Fore.RESET)
            print "==== POWERUP QUESTION ===="
            print "%s " % (powerupq['text'])
            cont = 0
            for answer in powerupq['answers']:
                if cont == correcta:
                    print (Fore.GREEN + "%s. %s" % (cont,answer))
                else:
                    print (Fore.RED + "%s. %s" % (cont,answer))
                cont += 1
            print (Fore.RESET)

        # ptsout.close()


def request(context, flow):
    #pprint (vars(flow.request))
    #ppriint(vars(context))
    #print "=================="
    pass
