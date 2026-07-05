import os

lista_de_convidados = ['Ana', 'Pedro', 'Carlos']

def adicionar_convidado():
	print(f'Lista atual de convidados: {lista_de_convidados}')
	nome_convidado = str(input('Digite o nome do novo convidado: '))
	if not nome_convidado.isalpha():
		print('Digite apenas nomes válidos.')
		adicionar_convidado()
	try:
		posição = int(input('Digite a posição na qual deseja inserir o convidado: '))
	except ValueError:
		print('Digite apenas uma posição válida.')
		adicionar_convidado()
	posição_verdadeira = posição - 1
	lista_de_convidados.insert(posição_verdadeira, nome_convidado)
	print(f'Lista atualizada de convidados: {lista_de_convidados}')
	



def main():
	os.system('cls')
	adicionar_convidado()

if __name__ == '__main__':
	main()