# Ricardo Castro

def converter(numero, base_origem, base_destino):
    # Primeiro converte para decimal
    decimal = int(numero, base_origem)

    # Depois converte para a base desejada
    if base_destino == 2:
        return bin(decimal)[2:]   # Binário
    elif base_destino == 8:
        return oct(decimal)[2:]   # Octal
    elif base_destino == 16:
        return hex(decimal)[2:].upper()  # Hexadecimal
    else:
        return str(decimal)       # Decimal

def menu():
    print("=== Calculadora de Conversão ===")
    print("Escolha a base de origem:")
    print("1 - Decimal")
    print("2 - Binário")
    print("3 - Octal")
    print("4 - Hexadecimal")

    origem = int(input("Digite o número da opção: "))
    numero = input("Digite o número: ")

    print("\nEscolha a base de destino:")
    print("1 - Decimal")
    print("2 - Binário")
    print("3 - Octal")
    print("4 - Hexadecimal")

    destino = int(input("Digite o número da opção: "))

    # Dicionário para mapear opções
    bases = {1: 10, 2: 2, 3: 8, 4: 16}

    resultado = converter(numero, bases[origem], bases[destino])
    print(f"\nResultado: {resultado}")

# Programa principal
menu()
