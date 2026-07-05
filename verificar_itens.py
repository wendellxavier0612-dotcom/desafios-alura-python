despensa = ['sal', 'trigo', 'ovos']

def verificar_item():
	try:
		item_verificar = str(input('Digite o item que você quer verificar: ')).lower()
		if not item_verificar in despensa:
			print(f'O {item_verificar} precisa ser comprado.')
		else:
			print(f'O {item_verificar} está na despensa.')
	except ValueError:
		print('Digite um nome válido do item à verificar')

def main():
	verificar_item()

if __name__ == '__main__':
	main()