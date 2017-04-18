import json
import random
import batalha #funcao batalha
import pet #programa que permite a escolha do seu inspermon inicial
import time

with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)

vidaj = pet.pet['vida']
poderj = pet.pet['poder']
defesaj = pet.pet['defesa']
fugirLista = [1,2,3,4,5] #lista que define a chance de fugir, no caso 1/5

#codigo basico
while True:
	x = random.choice(a)
	pergunta = input("passear ou dormir? ")
	if pergunta == "dormir":
		print("Até mais")
		break
	elif pergunta == "passear":
		print("um {0} muito louco brotou do nada\n vida: {1}\n poder: {2}\n defesa: {3}".format(x['nome'], x['vida'],x['poder'],x['defesa']))
		time.sleep(2)
		resposta = input('Você deseja batalhar ou fugir? ') #opcao de fuga
		if resposta == 'fugir':
			z = random.choice(fugirLista)
			if z == 1:
				print('Você fugiu')
				continue

			else:
				print('Não foi possível fugir nesse momento')
				print('A batalha continua e voce perdeu seu round de ataque')
				resultado = batalha.battleY(x['vida'],vidaj,poderj,defesaj,x['defesa'],x['poder'], x['nome'])
				if resultado == "você perdeu":
					print('voce morreu, seu noob')
					time.sleep(3)
					print('GAME OVER')
					break
				else:
					print("você ganhou")
					pet.pet['xp'] = pet.pet['xp'] + 5
					print("você recebeu 5 xp")
					print(pet.pet)



		elif resposta == 'batalhar':
			resultado = batalha.battle(x['vida'],vidaj,poderj,defesaj,x['defesa'],x['poder'],x['nome'])
			if resultado == "você perdeu":
				print('voce morreu, seu noob')
				time.sleep(3)
				print('GAME OVER')
				break
			else:
				print("você ganhou")
				pet.pet['xp'] = pet.pet['xp'] + 5
				print("você recebeu 5 xp")
				print(pet.pet)
		else:
			print("ERRO, reposta invalida, tente novamente")

	else:
		print("ERRO, reposta invalida, tente novamente")
		continue 

