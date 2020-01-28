#!/usr/bin/python 
#coding: utf-8

import socket, os, time, sys

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'

print (B+G+"> Portscanner Console")

q = '[$] T@rget p0rts: '
ports = list(map(int, input(q).split(' ')))

website = input('[$] Websit3: ')

os.system('clear')

print (B+R+ "[#] The verification started on " + website + " || Port: " + str(ports))

time.sleep(2)

try:
# Here is where the magic happens
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((website, port))
        if code == 0:
            print(port, 'OPEN')
        else:
            print(port, 'THIS PORT IS NOT OPEN')
except:
    print('[!] THERE IS AN ERROR')

time.sleep(0.3)
sys.exit(1)