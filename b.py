import json
import random
import batalha
import pet
with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)
vidaj = pet.pet['vida']
poderj = pet.pet['poder']
defesaj = pet.pet['defesa']
fugirLista = [1,2,3,4,5]
while True:
	x = random.choice(a)
	pergunta = input("passear ou dormir? ")
	if pergunta == "dormir":
		print("Até mais")
		break
	elif pergunta == "passear":
		print("um {0} muito louco brotou do nada".format(x['nome']))
		resposta = input('Você deseja batalhar ou fugir? ')  
		if resposta == 'fugir':
			z = random.choice(fugirLista)
			if z == 1:
				print('Você fugiu')
				continue
			else:
				print('Não foi possível fugir nesse momento')
				print('A batalha continua')
				print(batalha.battleY(x['vida'],vidaj,poderj,defesaj,x['defesa'],x['poder']))

		elif resposta == 'batalhar':
			print(batalha.battle(x['vida'],vidaj,poderj,defesaj,x['defesa'],x['poder']))
	

	else:
		print("ERRO, reposta invalida, tente novamente")
		continue 

