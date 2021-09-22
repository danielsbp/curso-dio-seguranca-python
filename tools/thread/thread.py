from threading import Thread
import time

def carro(velocidade, piloto):
	trajeto = 0
	while trajeto <= 100:
		
		
		time.sleep(0.5)

		print('Piloto: {} km: {} \n'.format(piloto, trajeto))
		trajeto += velocidade
		if(trajeto == 100):
			print("O piloto {} alcançou a linha de chegada!".format(piloto))

t_carro1 = Thread(target = carro, args=[1, "Bruno"])
t_carro2 = Thread(target = carro, args=[2, "Douglas"])

t_carro1.start()
t_carro2.start()