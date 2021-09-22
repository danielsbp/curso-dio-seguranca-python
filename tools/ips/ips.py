# Permite a manipulação de IP;
import ipaddress

rede = '192.168.0.0/4'

endereco = ipaddress.ip_network(rede, strict=False)

for ip in endereco:
	print("IP: ",ip)
print(endereco)