#!/usr/bin/python 
#coding: utf-8
#Author: n3o (Renan)
from ptcore import *
import socket, os, time, sys

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'

os.system('clear')

print (B+G+'[!] The scan started on {0}:{1} | {2}-{3}-{4}'.format(hour, minute, day, month, year))

def main():
    
    print(banner)
    portscan = input(G+"\nPortscanner Console > ")
    if portscan == '1' or portscan == '01':
        try:
            q =  '[$] T@rget p0rts: '
            ports = list(map(int, input(q).rstrip().split(' ')))
            
            #milliseconds
            delay = float(input('[$] S3t th3 t1m30ut: '))
            
        except ValueError:
            print(R+'\n[!] Wrong Input \n')
            print(R+'[!] Restarting...')
            time.sleep(1)
            restart_program()
            
        website = input('[$] Websit3 or IP: ')
        
        print (B+G+ "\n[#] The verification started on " + website + " || Port: " + str(ports))
        
        time.sleep(2)
        
        # Here is where the magic happens
        try:
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(delay)
                code = client.connect_ex((website, port))
                if code == 0:
                    print(str(port), 'OPEN')
                else:
                    print(str(port), 'CLOSE')
                    
        except:
            print(R+'\n[!] There is an error')
            print(R+'[!] Restarting...')
            time.sleep(1)
            restart_program()
             
        p = list(map(int, ports))
        
        ## Saving it into a file ##
        with open('portscan.txt', 'w') as scan_list:
            scan_list.write(str(website) +'\n')
        
        for scan in p:
            with open('portscan.txt', 'at') as f:
                f.write(str(scan)+' PORT CHECKED'+'\n')        
        scan_list.close()
        ###########################
        
        print(B+G+'\n~#~ Ports written in portscan.txt \n')
        
       
        time.sleep(0.3)
        sys.exit(1)
         
    elif portscan == '2' or portscan == '02':
        time.sleep(0.3)
        sys.exit(1)
    else:
        print(R+'[!] Wrong Input\n')
        print('[!]Restarting...\n')
        restart_program()
              
if __name__ == '__main__':
    main()