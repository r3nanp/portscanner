#!/usr/bin/python 
#coding: utf-8
#Author: n3o (Renan)

import socket, os, time, sys, threading

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'

### Code time ######
from datetime import datetime
now = datetime.now()
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year
##################

os.system('clear')

print (B+G+'[!] The scan started on {0}:{1} | {2}-{3}-{4}'.format(hour, minute, day, month, year))
print('\n')
print (B+G+"> Portscanner Console")

q = '[$] T@rget p0rts: '
ports = list(map(int, input(q).split(' ')))

website = input('[$] Websit3 or IP: ')

delay = float(input('S3t th3 t1m30ut: '))

print('\n')

def main():
    TCPsock.settimeout(delay)

print (B+G+ "[#] The verification started on " + website + " || Port: " + str(ports))

time.sleep(2)

# Here is where the magic happens
try:
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(delay)
        code = client.connect_ex((website, port))
        if code == 0:
            print(port, 'OPEN')
        else:
            print(port, 'THIS PORT IS NOT OPEN')
except:
    print('[!] THERE IS AN ERROR')
    
## Saving it into a file ##
scan_list = open('portscan.txt', 'w')
for scan in ports:
    scan_list.write(str(website) +'\n')
    scan_list.write(str(scan)+'\n')    
scan_list.close()
###########################

print('\n')

print(B+G'~#~ Ports written in portscan.txt \n')
    

time.sleep(0.3)
sys.exit(1)
