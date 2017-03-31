import json
import random
import batalha
import pet
with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)
vidaj = pet.pet['vida']
poderj = pet.pet['poder']
defesaj = pet.pet['defesa']
while True:
	x = random.choice(a)
	pergunta = input("passear ou dormir? ")
	if pergunta == "dormir":
		print("Até mais")
		break
	elif pergunta == "passear":
		print("Voce ira batalhar com {0}".format(x['nome']))
		print(batalha.battle(x['vida'],vidaj,poderj,defesaj,x['defesa'],x['poder']))
		break
	else:
		print("ERRO, reposta invalida, tente novamente")
		continue 

