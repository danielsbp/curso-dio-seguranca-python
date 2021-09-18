import socket
import sys #Fornece o acesso a algumas variáveis e funções que tem forte interação com o interpretador.

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	except socket.error as e:
		print("A conexão falhou.")
		print("Erro: {}".format(e))
		sys.exit()

	print("Socket criado com sucesso.")

	host = input("Digite o IP ou HOST a ser conectado: ")
	port = input("Digite a porta TCP a ser conectada: ")

	try:
		s.connect((host, int(port)))
		# Se conectado, significa que os dados estão sendo transmitidos de forma correta.
		print("Cliente TCP conectado com sucesso no host {}.".format(host+":"+port))
		s.shutdown(2)
	except socket.error as e:
		print("Houve um problema na conexão com o host: {}.".format(host+":"+port))
		print("Erro: {}".format(e))
		sys.exit() # Sai da aplicação.

if __name__ == "__main__":
	main()


