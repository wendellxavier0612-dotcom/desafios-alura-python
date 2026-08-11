import os

def quantidade_caracteres():
	frase = input('Digite uma palavra: ')
	print(f'Essa palavra tem {len(frase)} caracteres')
def main():
	os.system('cls')
	quantidade_caracteres()
if __name__ == '__main__':
	main()