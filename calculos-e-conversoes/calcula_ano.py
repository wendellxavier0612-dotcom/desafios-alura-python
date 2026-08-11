import os

def anos():
	try:
		ano_nascimento = int(input('Digite o ano de nascimento: '))
		ano_atual = int(input('Digite o ano atual: '))
		calculo = ano_atual - ano_nascimento
		if ano_atual - ano_nascimento == 1:
			os.system('cls')
			print('A idade é 1 ano')
		elif ano_atual - ano_nascimento > 120 or ano_atual - ano_nascimento < 1:
			os.system('cls')
			print(f'Idade irreal: {calculo}')
			anos()
		elif ano_atual < ano_nascimento:
			os.system('cls')
			print('O ano de nascimento tem que ser menor que o ano atual')
			anos()
		else:
			os.system('cls')
			print(f'A idade é {calculo} anos')
	except ValueError:
		os.system('cls')
		print('Erro! Por favor, insira somente números')
		anos()
def main():
	os.system('cls')
	anos()
if __name__ == '__main__':
	main()