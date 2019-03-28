#Hacer PING

import os
def ping(ip):
  response = os.system("ping -c 10 " + ip + " >test%s.txt"%i)

  #and then check the response...
  if response == 0:
    print (ip, 'is up!')
  else:
    print (ip, 'is down!')

for i in range(1,33):
  ping("google.com")