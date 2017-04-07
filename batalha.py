def battle(vida_oponente,vida_jogador, poder_jogador,defesa_jogador, defesa_oponente, poder_oponente):
	while vida_jogador > 0 and vida_oponente > 0:
		x = poder_jogador - defesa_oponente
		if x <= 0:
			x = 0
		vida_oponente = vida_oponente - (x)
		if vida_oponente <= 0:
			return "você ganhou"
          
		y = poder_oponente - defesa_jogador
		if y <= 0:
			y = 0
		vida_jogador = vida_jogador - (y)
		if vida_jogador <= 0:
			return "você perdeu"

def battleY(vida_oponente,vida_jogador, poder_jogador,defesa_jogador, defesa_oponente, poder_oponente):
	while vida_jogador > 0 and vida_oponente > 0:	
		y = poder_oponente - defesa_jogador
		if y <= 0:
			y = 0
		vida_jogador = vida_jogador - (y)
		if vida_jogador <= 0:
			return "você perdeu"
		x = poder_jogador - defesa_oponente
		if x <= 0:
			x = 0
		vida_oponente = vida_oponente - (x)
		if vida_oponente <= 0:
			return "você ganhou"
					