import os
def produtos():
	try:
		nome_produtos = input('Digite o nome dos produtos separados por vírgula: ').split(',')
		valores = input('Digite o valor dos produtos respectivamente separados por vírgula: ').split(',')
		try:		
			for valor in valores:
				valor = int(valor)
		except ValueError:
				nome_produtos.clear()
				valores.clear()
				print('Digite apenas valores válidos')
				produtos()
		for produto, valor in zip(nome_produtos, valores):
			print(f'{produto.strip()}: {valor.strip()}')
	except ValueError:
		nome_produtos.clear()
		valores.clear()
		print('Digite apenas valores válidos')
		produtos()
def main():
	os.system('cls')
	produtos()
if __name__ == "__main__":
	main()