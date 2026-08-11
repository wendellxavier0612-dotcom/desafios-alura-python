import random
import os

def jogo_numero_secreto():
	numero_secreto = random.randint(1, 100)
	palpite = ''
	tentativas = 0
	while palpite != numero_secreto:
			try:
				palpite = int(input('Digite o seu palpite entre 1 e 100: '))
				if palpite < 1 or palpite > 100:
					print('Entrada inválida: número fora do intervalo! Digite um número entre 1 e 100.')
				elif palpite > numero_secreto:
					print('O número é menor, tente novamente.')
					tentativas += 1 
				elif palpite < numero_secreto:
					print('O número é maior')
					tentativas += 1
				else:
					print(f'Você acertou! O número secreto era {numero_secreto} e você o descobriu com {tentativas} tentativas')
					jogar_novamente_jogo()
					break
					
			except ValueError:
				print('Entrada inválida: digite apenas números entre 1 e 100')

def jogar_novamente_jogo():
	jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
	if jogar_novamente == 's':
		jogo_numero_secreto() # Chama para iniciar um novo jogo
	else:
		print("Obrigado por jogar!")

def main():
	os.system('cls')
	jogo_numero_secreto()

if __name__ == '__main__':
	main()
