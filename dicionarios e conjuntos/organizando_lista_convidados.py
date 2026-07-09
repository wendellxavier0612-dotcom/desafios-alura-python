convidados = {}

def adicionar_convidados():
	nome_convidado = input('Digite o nome do convidado: ')
	if nome_convidado.lower() == 'sair':
		chaves = convidados.keys()
		print(f'Convidados confirmados: {', '.join(chaves)}')
	elif not nome_convidado.isalpha() or nome_convidado == '':
		print('Digite apenas nomes válidos.')
		adicionar_convidados()
	else:
		convidados[nome_convidado] = 'Convidado'
		adicionar_convidados()

adicionar_convidados()