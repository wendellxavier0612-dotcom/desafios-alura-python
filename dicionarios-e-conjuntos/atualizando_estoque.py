estoque = { 
    "Caderno universitário": 50, 
    "Caneta azul": 120, 
    "Borracha branca": 30 
}

def atualizar_estoque():
	try:
		produto = str(input('Nome do produto a ser atualizado: '))
		quantidade = int(input('Nova quantidade: '))
		if not produto in estoque:
			print('Digite um produto que já consta no estoque.')
			atualizar_estoque()
		else:
			estoque.update({f'{produto}': quantidade})
			print(estoque)
	except ValueError:
		print('Digite ao menos um produto válido para atualizar o estoque.')
	

atualizar_estoque()