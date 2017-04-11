import json

with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)
while True:
	print("esses são os inspèrmons disponíveis: xamando, picaxu e pidjet")
	b = input("escolha um dos inspèrmons disponíveis: ")
	if b =="picaxu":
		pet = a[0]
		break
	elif b == "xamando":
		pet = a[1]
		break
	elif b == "pidjet":
		pet = a[2]
		break
	else:
		print("ERRO, reposta invalida, tente novamente")
		continue

print("esses são os status do seu novo inspèrmon: \n nome: {0} \n vida: {1} \n poder: {2} \n defesa: {3} ". format(pet['nome'],pet['vida'],pet['poder'],pet['defesa']))
