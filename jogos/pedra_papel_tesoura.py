import random
import os


def escolha_usuário():
	escolhas_computador = ['pedra', 'papel', 'tesoura']
	escolha_maquina = random.choice(escolhas_computador)
	escolha = str(input('Escolha uma opção (Pedra, Papel, Tesoura): ')).lower()
	
	if escolha == escolha_maquina:
		print(f'Houve empate, máquina também escolheu: {escolha_maquina}')
		escolha_usuário()
	elif escolha == 'papel' and escolha_maquina == 'tesoura':
		print(f'Você perdeu, máquina escolheu: {escolha_maquina}')
	elif escolha == 'pedra' and escolha_maquina == 'papel':
		print(f'Você perdeu, máquina escolheu: {escolha_maquina}')
	elif escolha == 'tesoura' and escolha_maquina == 'pedra':
		print(f'Você perdeu, máquina escolheu: {escolha_maquina}')
	elif escolha == 'papel' and escolha_maquina == 'pedra':
		print(f'Você ganhou, máquina escolheu: {escolha_maquina}')
	elif escolha == 'pedra' and escolha_maquina == 'tesoura':
		print(f'Você ganhou, máquina escolheu: {escolha_maquina}')
	elif escolha == 'tesoura' and escolha_maquina == 'papel':
		print(f'Você ganhou, máquina escolheu: {escolha_maquina}')
	else:
		print('Insira apenas opções válidas!')
		escolha_usuário()

def main():
	os.system('cls')
	escolha_usuário()

if __name__ == '__main__':
	main()