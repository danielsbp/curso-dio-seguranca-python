import socket

#Objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso.")

host = "localhost"
port = 5432

#.bind() - faz uma ligação através do host e do port
s.bind((host, port))
mensagem = "\nServidor: Olá cliente!"

while 1:
	dados, end = s.recvfrom(4096)

	if dados:
		print("Servidor enviando mensagem...")
		s.sendto(dados + (mensagem.encode()), end)