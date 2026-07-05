lista = ['Ana', 'Carlos', 'Pedro']
def corrigir_posições():
	nome_incorreto = str(input('Digite o nome incorreto: '))
	if not nome_incorreto.isalpha():
		print('Digite apenas nomes válidos.')
		corrigir_posições()
	nome_correto = str(input('Digite o nome correto: '))
	if not nome_correto.isalpha():
		print('Digite apenas nomes válidos.')
		corrigir_posições()
	if nome_incorreto in lista:
		posição = lista.index(nome_incorreto)
		lista.remove(nome_incorreto)
		lista.insert(posição, nome_correto)
		print(f'O nome {nome_incorreto} foi substituído por {nome_correto}')
		print(f'Lista atualizada: {lista}')
	else:
		print('Nenhum nome incorreto foi encontrado na lista')
corrigir_posições()

