import os
import time 

print("#"*60)
print("Ferramenta de ping multiplo")
print("#"*60)

with open("hosts.txt") as file:
	dump = file.read()
	dump = dump.splitlines()
	for ip in dump:
		print()
		print("-"*60)
		print(" \"Pingando\" em {}".format(ip))
		os.system('ping {}'.format(ip))
		print()
		print("Ping em {} foi finalizado!".format(ip))
		time.sleep(5)