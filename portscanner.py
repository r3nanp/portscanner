''' Todos os direitos reservados a Renan Pereira de Souza '''
import socket 

doors = [21, 23, 80, 443, 8080, 3306]
for door in doors:
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(0.1)
	codigo = cliente.connect_ex(('http://example.com', door))
	if codigo == 0:
		print door, 'OPEN'
