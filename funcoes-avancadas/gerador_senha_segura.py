import os
import random


minúsculas = 'abcdefghijklmnopqrstuvwxyz'
maiúsculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
números = '0123456789'
símbolos = '!@#$%&*'

senha_aleátoria = [
	random.choice(minúsculas),
	random.choice(maiúsculas),
	random.choice(números),
	random.choice(símbolos)
]
def gerador_senha():
	letra_minúscula2 = random.choice(minúsculas)
	senha_aleátoria.append(letra_minúscula2)
	letra_minúscula3 = random.choice(minúsculas)
	senha_aleátoria.append(letra_minúscula3)
	letra_maiúscula2 = random.choice(maiúsculas)
	senha_aleátoria.append(letra_maiúscula2)
	letra_maiúscula3 = random.choice(maiúsculas)
	senha_aleátoria.append(letra_maiúscula3)
	número2 = random.choice(números)
	senha_aleátoria.append(número2)
	número3 = random.choice(números)
	senha_aleátoria.append(número3)
	caractere_especial2 = random.choice(símbolos)
	senha_aleátoria.append(caractere_especial2)
	caractere_especial3 = random.choice(símbolos)
	senha_aleátoria.append(caractere_especial3)
	random.shuffle(senha_aleátoria)
	senha_gerada = "".join(senha_aleátoria)
	print(f'Senha gerada: {senha_gerada}')









def main():
	os.system('cls')
	gerador_senha()


if __name__ == '__main__':
	main()