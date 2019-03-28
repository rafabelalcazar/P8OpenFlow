# Title:        ping.py
# Description:  Este codigo ejecuta NUM_HILOS para representar los usuarios que hacen ping a el host con IP
# '1345.2345.2345' y lo hace 32 veces para hacer estadisticas de como se comporta la red
# cuando el trafico aumenta:  practica 4 de enfasis3 de la UNICAUCA
# Author:       Rafael Alejandro Belalcazar Burbano
# Date:         15-03-2019

import os
def ping(ip):
  response = os.system("ping -c 32 " + ip + " >test%s.txt"%i)

  #and then check the response...
  if response == 0:
    print (ip, 'is up!')
  else:
    print (ip, 'is down!')

for i in range(1,33):
  ping("google.com")