import os

cédulas_disponíveis = [100, 50, 20, 10, 5, 2]

valor_saque = int(input('Digite o valor do saque: '))

def calculo(valor_saque):
	for cedula in cédulas_disponíveis:
		quantidade_de_cedulas = valor_saque // cedula
		if quantidade_de_cedulas > 0:
			print(f"{quantidade_de_cedulas} de R$ {cedula}")
			valor_saque = valor_saque % cedula

				

def saque(valor_saque):
	if valor_saque % 2 == 0:
		calculo(valor_saque)
	else:
		print('Erro: O valor deve ser múltiplo de 2.')




def main():
	os.system('cls')
	saque(valor_saque)


if __name__ == '__main__':
	main()