import os

def saudação():
	try:
		hora = float(input('Digite a hora atual (0-23):'))
		if hora > 5 and hora < 12:
			print('Bom dia!')
		elif hora >= 12 and hora < 18:
			print('Boa tarde!')
		elif hora >= 18 and hora <= 23:
			print('Boa noite!')
		elif hora >= 0 and hora <= 5:
			print('Boa noite!')
		elif hora > 23:
			print('Digite apenas números válidos(0-23)')
			saudação()
	except ValueError:
		print('Digite apenas números válidos(0-23)')
		saudação()
def main():
	os.system('cls')
	saudação()
if __name__ == '__main__':
	main()