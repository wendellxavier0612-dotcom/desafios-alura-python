import os

tarefas = []

def adicionar_tarefa():
	os.system('cls')
	tarefa_adicionar = str(input('Digite a tarefa: '))
	tarefas.append(tarefa_adicionar)
	print('Tarefa adicionada!')
	retornar_tela_inicial()

def visualizar_tarefas():
	os.system('cls')
	print('Tarefas: ')
	for numero, tarefa in enumerate(tarefas, start=1):
		print(f'{numero}. {tarefa}')
	retornar_tela_inicial()

def remover_tarefa():
	os.system('cls')
	if len(tarefas) == 0:
		print('Nenhuma tarefa para remover')
		retornar_tela_inicial()
	else:
		pass
	try:
		posicao_falsa = int(input('Digite o número da tarefa a ser removida: '))
		posicao_verdadeira = posicao_falsa - 1
		if 0 <= posicao_verdadeira < len(tarefas):
			tarefa_removida = tarefas.pop(posicao_verdadeira)
			print(f'Tarefa {tarefa_removida} removida!')
			retornar_tela_inicial()
		else:
			print('Digite o número da tarefa válida.')
			retornar_tela_inicial()
	except ValueError:
		os.system('cls')
		print('Digite apenas números válidos correspondentes à tarefa que deseja remover.')
		retornar_tela_inicial()

def encerrar_programa():
	os.system('cls')
	print('Saindo do gerenciador de tarefas. Até mais!')

def retornar_tela_inicial():
	input('Digite qualquer tecla para retornar a tela inicial')
	tela_inicial()


def tela_inicial():
	print('1. Adicionar tarefa')
	print('2. Visualizar tarefas')
	print('3. Remover tarefa')
	print('4. Sair')
	try:
		escolha_inicial = int(input('Escolha uma opção: '))
		if escolha_inicial == 1:
			adicionar_tarefa()
		elif escolha_inicial == 2:
			visualizar_tarefas()
		elif escolha_inicial == 3:
			remover_tarefa()
		elif escolha_inicial == 4:
			encerrar_programa()
		else:
			os.system('cls')
			print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
			tela_inicial()
	except ValueError:
		os.system('cls')
		print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
		tela_inicial()

def main():
	os.system('cls')
	tela_inicial()

if __name__ == '__main__':
	main()