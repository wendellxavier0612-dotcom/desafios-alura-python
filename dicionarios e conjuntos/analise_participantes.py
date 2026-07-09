participantes = { 
    "Mariana": 25, 
    "Carlos": 32, 
    "Beatriz": 28, 
    "Rafael": 35 
}
print(f'Nome dos participantes: {", ".join(participantes.keys())}')
print(f'Idade dos participantes: {", ".join(str(idade) for idade in participantes.values())}')
print('Participantes e suas idades:\n')
for participante in participantes:
	print(f'- {participante}: {participantes[participante]} anos')

