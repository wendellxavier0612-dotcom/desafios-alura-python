import os
def receber_dados():
	try:
		valores = input('Digite os valores das vendas separando-os por espaços em branco e utilizando . no lugar da vírgula para valores decimais: ').split()
		valores_convertidos = list(map(float, valores))
		for valor in valores_convertidos:
			if valor < 0:
				print('Valores negativos não podem ser somados!')
				receber_dados()
				break
		soma_total = sum(valores_convertidos)
		print(f'O valor total das vendas é de: {soma_total}')
	except ValueError:
		print('Digite somente valores válidos!')
		receber_dados()
def main():
	os.system('cls')
	receber_dados()
if __name__ == '__main__':
	main()