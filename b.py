import json
import random

with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)

while True:
	pergunta = input("passear ou dormir? ")
	if pergunta == "dormir":
		print("Até mais")
		break
	elif pergunta == "passear":
		print("uma batalha acontecera aqui")
	else:
		print("ERRO, reposta invalida, tente novamente")
		continue 
	
	
