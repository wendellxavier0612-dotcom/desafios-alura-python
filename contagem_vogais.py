import os

def contandor_vogais():

		texto = str(input('Digite uma frase para a contagem de vogais: '))
		texto_limpo = texto.replace(' ', '').lower()
		vogais = 'aeiou'
		contador = 0
		for letra in texto_limpo:
			if letra in vogais:
				contador += 1
		print(f'A quantidade de vogais na frase é de: {contador}')







def main():
	os.system('cls')
	contandor_vogais()
if __name__ == '__main__':
	main()