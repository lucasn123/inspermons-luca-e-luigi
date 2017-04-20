import json
import random
import batalha #funcao batalha
import pet #programa que permite a escolha do seu inspermon inicial
import time
import evolucao #programa que permite a evolucao dos inspermons

with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)

listainsperdex = [] #guarda os dicionarios de todos inspermons ja encontrados
vidaj = pet.pet['vida']
poderj = pet.pet['poder']
defesaj = pet.pet['defesa']
fugirLista = [1,2,3,4,5] #lista que define a chance de fugir, no caso 1/5
x = 0

while True:
	
	pergunta = input("passear / dormir / insperdex: ")
	if pergunta == "dormir":
		print("Até mais")
		break
	elif pergunta == "passear":
		x = random.choice(a) #escolhe um inspermon aleatorio a partir do arquivo json
		if x not in listainsperdex:
			listainsperdex.append(x) #adiciona inspermons encontrados em uma lista
		print("um {0} muito louco brotou do nada\n vida: {1}\n poder: {2}\n defesa: {3}".format(x['nome'],x['vida'],x['poder'],x['defesa']))
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
				time.sleep(1)
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
					if pet.pet['xp'] == 40:
						print(evolucao.evolucao(wild_inspermons, pet))
						print("esses são os status do seu novo inspèrmon: \n nome: {0} \n vida: {1} \n poder: {2} \n defesa: {3} ". format(pet.pet['nome'],pet.pet['vida'],pet.pet['poder'],pet.pet['defesa']))
					
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
				if pet.pet['xp'] == 40:
					print(evolucao.evolucao(wild_inspermons, pet))
					print("esses são os status do seu novo inspèrmon: \n nome: {0} \n vida: {1} \n poder: {2} \n defesa: {3} ". format(pet.pet['nome'],pet.pet['vida'],pet.pet['poder'],pet.pet['defesa']))
				
		else:
			print("ERRO, resposta invalida")

	elif pergunta == 'insperdex':
		print ("INSPERDEX")
		print("\nEsses são os status do seu inspèrmon: \n nome: {0} \n vida: {1} \n poder: {2} \n defesa: {3} \n xp: {4} \n". format(pet.pet['nome'],pet.pet['vida'],pet.pet['poder'],pet.pet['defesa'], pet.pet['xp']))
		print ("Esses são os inspèrmons que você já encontrou:")
		if x == 0: #no caso de o usuario acessar a insperdex antes de 'passear'
			print("    novos inspèrmons não foram encontrados \n")	
		else:
			for i in listainsperdex: #acessa a lista dos inpermons encontrados	
				print("-------------\n nome: {0} \n vida: {1} \n poder: {2} \n defesa: {3} ".format(i['nome'],i['vida'],i['poder'],i['defesa']))

	else:
		print("ERRO, reposta invalida, tente novamente")
		continue 

