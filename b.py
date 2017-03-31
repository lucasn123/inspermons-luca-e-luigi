import json
import random
import batalha

with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)

while True:
	x = random.choice(a)
	pergunta = input("passear ou dormir? ")
	if pergunta == "dormir":
		print("Até mais")
		break
	elif pergunta == "passear":
		print("Voce ira batalhar com {0}".format(x['nome']))
		print(batalha.battle(x['vida'],1000,1000,1000,x['defesa'],x['poder']))
		break
	else:
		print("ERRO, reposta invalida, tente novamente")
		continue 


