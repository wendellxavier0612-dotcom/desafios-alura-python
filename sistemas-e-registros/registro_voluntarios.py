import os
voluntários = []



def registro_voluntários():
	while True:
		registro = str(input('Digite o nome do voluntário (ou "sair" para encerrar): '))
		if not registro.isalpha():
			print('Apenas letras são válidas para o nome do voluntário.')
		elif registro.lower() == 'sair':
			print('Encerrando o programa')
			break
		else:
			voluntários.append(registro)
			print('Lista atualizada: ')
			print(f'Voluntários registrados: {voluntários}')
				
			
				
	





def main():
	os.system('cls')
	registro_voluntários()

if __name__ == '__main__':
	main()