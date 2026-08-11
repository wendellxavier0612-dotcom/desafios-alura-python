import os

def validar_cpf(cpf):
    # Primeiro, verifica se contém APENAS números
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    # Se passou na primeira, agora verifica o TAMANHO
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    # Se passou nas duas, é válido
    return "CPF válido."
 
cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))



def main():
	os.system('cls')
	validar_cpf()
if __name__ == '__main__':
	main()