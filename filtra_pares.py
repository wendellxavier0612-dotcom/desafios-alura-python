import os
numeros_pares = []

def filtrar_pares():
	try:
		numeros = input('Digite os números separando-os com espaço: ').split()
		for numero in numeros:
			numero = int(numero)
			if numero % 2 == 0:
				numero_par = numero
				numeros_pares.append(numero_par)
			numeros_como_string = [str(numero) for numero in numeros_pares] # Converte cada int para string
		print(f'Numeros pares: {numeros_como_string}')
	except ValueError:
		print("Digite apenas números válidos!")
		filtrar_pares()
def main():
	os.system('cls')
	filtrar_pares()
if __name__ == '__main__':
	main()