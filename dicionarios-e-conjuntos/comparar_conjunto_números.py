equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}
tarefas_juntas = set()

def comparar_conjuntos():
	tarefas_juntas = equipe_a.union(equipe_b)
	tarefa_remover = str(input('Digite o nome da tarefa que deseja remover: ')).lower()
	try:
		tarefas_juntas.remove(tarefa_remover)
	except KeyError:
		print('Digite uma tarefa válida.')


	print(tarefas_juntas)
	
	

comparar_conjuntos()
