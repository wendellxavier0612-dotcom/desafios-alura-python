import os
import csv

def retornar_ao_menu():
	input('Pressione qualquer tecla para retornar ao menu: ')


def registrar_notas():
	while True:
		try:
			aluno = input('Digite o nome do aluno(a): ')
			nota = float(input('Digite sua nota: '))
		except ValueError:
			print('Digite uma nota válida.')
			break
		with open('alunos.csv', 'a', newline='') as arquivo:
			escritor = csv.writer(arquivo)
			escritor.writerow([aluno, nota])
		print(f'Aluno(a): {aluno} foi registrado com a respectiva nota: {nota}')
		registrar_novamente = input('Você deseja registra outro aluno(a) (s/n)? ')
		if registrar_novamente.lower() == 's':
			continue
		else:
			break


def menu():
	while True:
		print('- CONTROLE DE NOTAS 2026 -\n')
		print('1. Registrar notas de um aluno.')
		print('2. Visualizar notas dos melhores alunos.')
		print('3. Encerrar o programa.')
		try:
			opcao = int(input('Digite a opção desejada: '))
		except ValueError:
			print('Digite uma opção válida.')
			continue
		if opcao == 1:
			registrar_notas()
		elif opcao == 2:
			try:
				with open('alunos.csv', newline='') as arquivo:
					leitor = csv.reader(arquivo)
					for dado in leitor:
						nota = float(dado[1])
						if nota >= 7:
							print(f'Aluno: {dado[0]} - Nota: {nota}')
			except FileNotFoundError:
				print('Nenhum aluno registrado ainda.')
			retornar_ao_menu()
		elif opcao == 3:
			print('Encerrando')
			break
		else:
			pass


def main():
	os.system('cls')
	menu()

if __name__ == '__main__':
	main()
