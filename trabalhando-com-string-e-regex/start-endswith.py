URL = str(input('Digite a URL para validação: '))
validacao = URL.startswith('https://') and URL.endswith('.com')

if validacao == False:
	print('URL inválida')
else:
	print('URL válida')