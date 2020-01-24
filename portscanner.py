import socket, os, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'


q = 'which ports do you wanna werify? '
ports = list(map(int, input(q).split(' ')))


website = input('what website you wanna verify? ')

os.system('clear')

print (B + "[#] The verification started on " + website + "|| Port: " + str(ports))

time.sleep(2)

os.system('clear')

# Here is where the magic happens
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((website, port))
    if code == 0:
        print(port, 'OPEN')
    else:
        print('THIS PORT IS NOT OPEN')
