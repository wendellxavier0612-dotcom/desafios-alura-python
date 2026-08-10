import re

padrao_regex = r"^[A-Z][a-z]+$"

nome = input('Digite o nome do cliente para a validação: ')

if re.fullmatch(rf'{padrao_regex}', nome):
	print('Nome válido!')
else:
	print('Nome inválido')