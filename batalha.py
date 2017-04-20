import time
import random
sorteLista = [0,1,2,3,4,5,6] #lista que define a probabilidade de 1/7 de ocorrer o critical hit

#funcao batalha com o jogador iniciando o ataque
def battle(vida_oponente,vida_jogador, poder_jogador,defesa_jogador, defesa_oponente, poder_oponente,nome_oponente):
    
	while vida_jogador > 0 and vida_oponente > 0:

		resposta2 = random.choice(sorteLista)
		if resposta2 == 6:
			print('Critical Hit !!')
			time.sleep(1)
			print("Seu ataque teve o dobro de dano!")
			x = poder_jogador*2 - defesa_oponente #o ataque critico multiplica em dois o poder de ataque
		else:
			x = poder_jogador - defesa_oponente #ataque normal
		if x <= 0:
			x = 1
		vida_oponente = vida_oponente - (x)
		print("Voce atacou {0}\n vida restante do oponente: {1}". format(nome_oponente,vida_oponente))
		time.sleep(1)
		if vida_oponente <= 0:
			return "você ganhou"
		resposta2 = random.choice(sorteLista)
		if resposta2 == 5:
			print('Critical Hit !!')
			time.sleep(1)
			print("voce sofreu o dobro de dano")
			y = poder_oponente*2 - defesa_jogador
		else:
			y = poder_oponente - defesa_jogador
		if y <= 0:
			y = 1
		vida_jogador = vida_jogador - (y)
		print("{0} atacou voce\n  sua vida restante: {1}". format(nome_oponente,vida_jogador))
		time.sleep(1)
		if vida_jogador <= 0:
			return "você perdeu"
            
			
#funcao batalha com o inimigo iniciando o ataque, no caso de tentativa de fuga falha
def battleY(vida_oponente,vida_jogador, poder_jogador,defesa_jogador, defesa_oponente, poder_oponente, nome_oponente):

	while vida_jogador > 0 and vida_oponente > 0:

		resposta2 = random.choice(sorteLista)
		if resposta2 == 5:
			print('Critical Hit !!')
			time.sleep(1)
			print("voce sofreu o dobro de dano")
			y = poder_oponente*2 - defesa_jogador
		else:
			y = poder_oponente - defesa_jogador
		if y <= 0:
			y = 1
		vida_jogador = vida_jogador - (y)
		print("{0} atacou voce\n  sua vida restante: {1}". format(nome_oponente,vida_jogador))
		time.sleep(1)
		if vida_jogador <= 0:
			return "você perdeu"

		resposta2 = random.choice(sorteLista)
		if resposta2 == 6:
			print('Critical Hit !!')
			time.sleep(1)
			print("Seu ataque teve o dobro de dano!")
			x = poder_jogador*2 - defesa_oponente
		else:
			x = poder_jogador - defesa_oponente
		if x <= 0:
			x = 1
		vida_oponente = vida_oponente - (x)
		print("Voce atacou {0}\n vida restante do oponente: {1}". format(nome_oponente,vida_oponente))
		time.sleep(1)
		if vida_oponente <= 0:
			return "você ganhou"
            


					