import os

print("#"*30)
print("Ferramenta de ping")
print("#"*30)

ip_or_host = input("Digite o IP ou Host a ser verificado: ")

os.system('ping -n 6 {}'.format(ip_or_host))

print("#"*30)
print("Fim da operação")