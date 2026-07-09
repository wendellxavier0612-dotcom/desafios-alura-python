lista_laura = set()
lista_ana = set()

def comparar_listas():
	itens_laura = input('Digite os itens da Laura: ').lower().split(', ')
	itens_ana = input('Digite os itens da Ana: ').lower().split(', ')
	for item in itens_laura:
		lista_laura.add(item)
	for item in itens_ana:
		lista_ana.add(item)
	itens_exclusivos_laura = lista_laura.difference(lista_ana)
	itens_exclusivos_ana = lista_ana.difference(lista_laura)
	lista_geral = lista_laura.intersection(lista_ana)
	if lista_geral == set():
		print('Nenhum item foi inserido nas listas.')
		comparar_listas()
	else:
		if len(lista_geral) == 1:
			print(f'Item em ambas listas: {lista_laura.intersection(lista_ana)}')
			print(f'Itens exclusivos da Laura: {itens_exclusivos_laura}')
			print(f'Itens exclusivos da Ana: {itens_exclusivos_ana}')
		else:
			print(f'Itens em ambas listas: {lista_laura.intersection(lista_ana)}')
			print(f'Itens exclusivos da Laura: {itens_exclusivos_laura}')
			print(f'Itens exclusivos da Ana: {itens_exclusivos_ana}')

comparar_listas()