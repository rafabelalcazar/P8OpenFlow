#Hacer PING

import os
import time

c = 0
def ping(ip):
  response = os.system("ping -c 1 " + ip)

  #and then check the response...
  if response == 0:
    print ip, 'is up!'
  else:
    print ip, 'is down!'

#Frecuencia para hacer ping
timeExper = 60.0  #Tiempo de experimento
peticiones = 100.0
fr =  timeExper/ peticiones


timeStart = time.time()
timeEnd = time.time() + timeExper
timeReq = timeStart + fr
while(timeEnd-timeStart > 0):
  
  timeStart = time.time()

  if(timeReq - timeStart <= 0):
    ping("192.168.43.84")
    timeReq= timeReq + fr    
    c=c+1
    print c #Para saber cuantos pings se han hecho
  
  #print timeEnd -timeStart