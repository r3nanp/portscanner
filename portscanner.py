from core import ptcore
import socket, os, time, sys

os.system('clear')
print(verf)

def main():
  print('\n'+banner)
  portscan = input('Portscanner> ')
  if portscan.strip() == '1' or portscan.strip() == '01':
    try:
      port =  '\n[$] T@rget p0rts: '

      ##Transform a string in a list of integer
      listPort = list(map(int, input(port).rstrip().split(' ')))

      #Milliseconds
      delay = float(input('[$] S3t th3 t1m30ut: '))

      except:
        wrongInput()

        website = input('[$] Websit3 or IP: ')

        print ('\n[#] The verification started on ' + website + ' || Port: ' + str(listPort))

        time.sleep(1)

        try:
          for port in listPort:
            # TCP/IP connection
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Timeout in ms
            client.settimeout(delay)
            code = client.connect_ex((website, port))
            if code == 0:
            #If the code is a 0, the port is open
              print(str(port), 'OPEN')
            else:
              print(str(port), 'CLOSE')

        except:
          wrongInput()

        ##Transform str in a list of int
        transformList = list(map(int, listPort))

        ## Saving it in a file ##
        try:
          with open('portscan.txt', 'w') as scan_list:
            scan_list.write(str(website) +'\n')

          for scan in transformList:
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
