import socket

# Criação do objeto de conexão.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado!")

host = "localhost"
port = 5433
mensagem = "Olá servidor!"

try:
	print("Cliente: "+mensagem)
	# Tentativa de enviar a mensagem empacotada para o servidor.
	#.sendto(<mensagem empacotada>, (<host>,<porta do servidor>)).
	s.sendto(mensagem.encode(), (host, 5432))
	#as duas variaveis vão receber uma mensagem do servidor.
	dados, servidor = s.recvfrom(4096)

	#a variável "dados" contém a mensagem empacotada, logo temos que dar um decode.
	dados = dados.decode()

	print("Cliente: "+dados)

finally:
	print("Cliente: Fechando a conexão.")
	#fecha a conexão.
	s.close()