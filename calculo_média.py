notas = input('Digite as notas separando-as por vírgula: ').split(", ")
notas = [float(nota) for nota in notas]
notas_somadas = sum(notas)
quantidade_de_notas = len(notas)
média = round(notas_somadas / quantidade_de_notas , 2)

print(f"Média final da turma: {média}")
