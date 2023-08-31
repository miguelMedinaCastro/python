#inserir um número inteiro e ele será dividido até chegar a 0.

num = int(input("Informe um número inteiro positivo: "))
while num >= 1:
    print("Resultado da divisão:", num)
    num = num / 2
print("Chegou a zero!")
