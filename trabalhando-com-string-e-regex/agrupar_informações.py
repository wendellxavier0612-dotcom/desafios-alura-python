import re


padrao_regex_nome = r"(\w+) (\w+) - (\d{4})"

entrada = input('Digite o nome completo e o ano de nascimento do paciente: ')
padrao = re.fullmatch(rf"{padrao_regex_nome}", entrada)
if padrao:
	primeiro_nome = padrao.group(1)
	sobrenome = padrao.group(2)
	ano = padrao.group(3)
	print(f'Primeiro nome: {primeiro_nome}')
	print(f'Sobrenome: {sobrenome}')
	print(f'Ano de nascimento: {ano}')
else:
	print('Formato inválido.')