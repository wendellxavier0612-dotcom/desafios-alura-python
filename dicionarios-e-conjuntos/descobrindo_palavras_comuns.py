texto1 = set()
texto2 = set()
def palavras_em_comum():
	primeiro_texto = str(input('Texto 1: ')).lower().split()
	segundo_texto = str(input('Texto 2: ')).lower().split()
	for palavra in primeiro_texto:
		texto1.add(palavra)
	for palavra in segundo_texto:
		texto2.add(palavra)
	mensagem = texto1.intersection(texto2)
	if mensagem == set():
		print('Nenhuma palavra em comum foi encontrada!')
	else:
		print(f'Palavras em comum: {texto1.intersection(texto2)}')

palavras_em_comum()