import time
def battle(vida_oponente,vida_jogador, poder_jogador,defesa_jogador, defesa_oponente, poder_oponente,nome_oponente):
	while vida_jogador > 0 and vida_oponente > 0:
		x = poder_jogador - defesa_oponente
		if x <= 0:
			x = 0
		vida_oponente = vida_oponente - (x)
		print("Voce atacou {0}\n vida restante do oponente: {1}". format(nome_oponente,vida_oponente))
		time.sleep(1)
		if vida_oponente <= 0:
			return "você ganhou"
          
		y = poder_oponente - defesa_jogador
		if y <= 0:
			y = 0
		vida_jogador = vida_jogador - (y)
		print("{0} atacou voce\n  sua vida restante: {1}". format(nome_oponente,vida_jogador))
		time.sleep(1)
		if vida_jogador <= 0:
			return "você perdeu"
			

def battleY(vida_oponente,vida_jogador, poder_jogador,defesa_jogador, defesa_oponente, poder_oponente, nome_oponente):
	while vida_jogador > 0 and vida_oponente > 0:	
		y = poder_oponente - defesa_jogador
		if y <= 0:
			y = 0
		vida_jogador = vida_jogador - (y)
		print("{0} atacou voce\n  sua vida restante: {1}". format(nome_oponente,vida_jogador))
		time.sleep(1)

		if vida_jogador <= 0:
			return "você perdeu"
		x = poder_jogador - defesa_oponente
		if x <= 0:
			x = 0
		vida_oponente = vida_oponente - (x)
		print("Voce atacou {0}\n vida restante do oponente: {1}". format(nome_oponente,vida_oponente))
		time.sleep(1)
		if vida_oponente <= 0:
			return "você ganhou"
					