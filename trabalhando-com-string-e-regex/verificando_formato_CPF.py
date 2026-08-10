import re

padrao_regex = r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"

cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX: ')

if re.fullmatch(rf'{padrao_regex}', cpf):
	print('CPF válido')
else:
	print('CPF inválido')