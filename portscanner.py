''' Todos os direitos reservados a Renan Pereira de Souza '''
import socket 

portas = [21, 23, 80, 443, 8080, 3306]
for porta in portas:
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(tempo)
	codigo = cliente.connect_ex(('http://exemplo.com', porta))
	if codigo == 0:
		print porta, 'OPEN'
