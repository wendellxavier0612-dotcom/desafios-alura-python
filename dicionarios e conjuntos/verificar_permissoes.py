permissoes_principais = {'leitura', 'escrita', 'execução', 'compartilhamento'}
permissoes = set()

def comparar_listas():
	permissoes_solicitadas = str(input('Digite qual as permissões solicitadas: ')).lower().split(', ')
	for permissao in permissoes_solicitadas:
		permissoes.add(permissao)
	diferencas = permissoes.difference(permissoes_principais)
	if len(diferencas) > 0:
		print('As permissões solicitadas não fazem parte das permissões principais.')
	else:
		print('As permissões solicitadas fazem parte das permissões principais.')
comparar_listas()