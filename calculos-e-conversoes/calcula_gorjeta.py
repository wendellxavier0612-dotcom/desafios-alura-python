#criar um programa que da gorjeta e mostra na tela do usuário o total da conta + gprjeta caso tenha
import os
'''
Primeira etapa: criar uma função main para captar todas as abas acessíveis do programa
'''

'''
Segunda etapa: criar uma função que irá receber os valores de valor total e valor da porcentagem da gorjeta
'''

def valores():
	valor_conta = float(input("Digite o valor total da conta: "))
	porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))
	gorjeta = (porcentagem_gorjeta / 100) * valor_conta
	valor_total = gorjeta + valor_conta
	print(f'Valor da gorjeta: {gorjeta:.2f}')
	print(f"O valor total a ser pago é de R${valor_total:.2f}")
def main():
	os.system('cls')
	valores()
	
if __name__ == '__main__':
	main()
