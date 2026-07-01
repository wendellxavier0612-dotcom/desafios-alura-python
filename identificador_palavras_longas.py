import os
palavras_longas = []

def identificar_palavras_longas():
	texto = list(str(input('Digite um texto: ')).split())
	try:
		for palavra in texto:
			if len(palavra) > 10:
				palavras_longas.append(palavra)
				mensagem = f'Palavras longas encontradas: {', '.join(palavras_longas)}'
		print(mensagem)
	except UnboundLocalError:
		print('Nenhuma palavra longa encontrada')
		identificar_palavras_longas()

	
		





def main():
	os.system('cls')
	identificar_palavras_longas()

if __name__ == '__main__':
	main()