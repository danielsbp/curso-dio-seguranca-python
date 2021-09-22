import random
import string

# Senhas seguras: >16 caracteres
tamanho = int(input("Digite o tamanho da senha: "))

chars = string.ascii_letters + string.digits + '!@#$%¨&*()_+´~]/;.,'
rnd = random.SystemRandom()
print(''.join(rnd.choice(chars) for i in range(tamanho)))