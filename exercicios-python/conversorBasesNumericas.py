#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Informe um número inteiro: "))
binario = ""
octal = ""
hexadecimal = ""

menu = True

while menu:
    print("[1] converter para BINÁRIO")
    print("[2] converter para OCTAL")
    print("[3] converter para HEXADECIMAL")
    escolha = int(input("Sua opção: "))

    if escolha == 1:
        numero = num
        while num > 0:
           restante = num % 2
           binario += str(restante)
           num = num // 2
           numInvertido = binario[::-1]
        print(f"{numero} convertido para BINÁRIO é igual a {numInvertido}")
        menu = False
    elif escolha == 2:
        numero = num
        while num > 0:
            restante = num % 8
            octal += str(restante)
            num = num // 8
            numInvertido = octal[::-1]
        print(f"{numero} convertido para OCTAL é igual a {numInvertido}")
        menu = False
    elif escolha == 3:
        print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
        menu = False
    else:
        print("Inválido!")
        menu = False

