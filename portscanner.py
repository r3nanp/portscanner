#coding: utf-8
#Author: n3o (Renan)
from ptcore import *
import socket, os, time, sys

os.system('clear')
print(verf)

def main():
    print('\n'+banner)
    portscan = input("Portscanner> ")
    if portscan.strip() == '1' or portscan.strip() == '01':
        try:
            q =  '\n[$] T@rget p0rts: '
            ##Transform str in a list of numbers
            ports = list(map(int, input(q).rstrip().split(' ')))
            
            #milliseconds
            delay = float(input('[$] S3t th3 t1m30ut: '))
            
        except:
            wrongInput()
            
        website = input('[$] Websit3 or IP: ')
        
        print ("\n[#] The verification started on " + website + " || Port: " + str(ports))
        
        time.sleep(1)
        
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
            wrongInput()

        ##Transform in a list    
        p = list(map(int, ports))
        
        ## Saving it into a file ##
        try:
            with open('portscan.txt', 'w') as scan_list:
                scan_list.write(str(website) +'\n')
        
            for scan in p:
                with open('portscan.txt', 'at') as f:
                    f.write(str(scan)+' PORT CHECKED'+'\n')        
        finally:
            scan_list.close()
        print(B+G+'\n~#~ Ports written in portscan.txt \n')
        exit()
        ###########################                      
         
    elif portscan.strip() == '2' or portscan.strip() == '02':
        exit()
    else:
        wrongInput()
              
if __name__ == '__main__':
    main()