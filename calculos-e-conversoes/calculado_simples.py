soma = lambda x, y: x + y
subtrai = lambda x, y: x - y
multiplica = lambda x, y: x * y
divide = lambda x, y: x / y

def calculo():
		while True:
			try:
				x = float(input('Digite o primeiro número: '))
		
				operador_matematico = input('Digite um operador matemático: ')
				

				y = float(input('Digite o segundo número: '))
				if operador_matematico == '+':
					print(soma(x, y))
					break
				elif operador_matematico == '-': 
					print(subtrai(x, y))
					break
				elif operador_matematico == '*': 
					print(multiplica(x, y))
					break
				elif operador_matematico == '/':
					print(divide(x, y))
					break
				else: 
					print('Opção inválida')
			except ZeroDivisionError:
				print('Erro: Divisão por zero não é permitida.')
			except ValueError:
				print('Erro: Entrada inválida. Digite apenas números.')
calculo()

