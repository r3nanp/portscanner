''' Todos os direitos reservados a Renan Pereira de Souza '''
import socket 

ports = [21, 23, 80, 443, 8080, 3306]
for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex(('http://example.com', port))
	if codigo == 0:
		print( port, 'OPEN')
