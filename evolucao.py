import pet
import json
with open ("inspermons.json") as wild_inspermons:
	a = json.load(wild_inspermons)

def evolucao(wild_inspermons, pet):
	if pet.pet['nome'] == "xamando":
		if pet.pet['xp'] == 40:
			pet.pet = a[7]
			return "xamando evoluiu para: charmelão!"
		elif pet.pet['nome'] == "charmelão":
			if pet.pet['xp'] == 40:
				pet.pet = a[4]
				return "charmelão evoluiu para: ayrizard!"

	elif pet.pet['nome'] == "pidjet":
		if pet.pet['xp'] == 40:
			pet.pet = a[5]
			return "pidjet evoluiu para : pidjao"
		elif pet.pet['nome'] == "pidjao":	
			if pet.pet['xp'] == 40:
				pet.pet = a[6]
				return "seu pidjao evoluiu para: pidjamelao!"

	elif pet.pet['nome'] == "picaxu":
		if pet.pet['xp'] == 40:
			pet.pet = a[1]
			return "picaxu evoluiu para : raiuuu!"
		