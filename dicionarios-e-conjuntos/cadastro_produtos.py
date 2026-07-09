produtos = {}

def cadastro_produtos():
	nome1 = str(input('Digite o nome do produto: '))
	quantidade1 = int(input(f'Digite a quantidade do produto {nome1}: '))
	produtos[nome1] = quantidade1
	nome2 = str(input('Digite o nome do produto: '))
	quantidade2 = int(input(f'Digite a quantidade do produto {nome2}: '))
	produtos[nome2] = quantidade2
	nome3 = str(input('Digite o nome do produto: '))
	quantidade3 = int(input(f'Digite a quantidade do produto {nome3}: '))
	produtos[nome3] = quantidade3
	print(produtos)

cadastro_produtos()