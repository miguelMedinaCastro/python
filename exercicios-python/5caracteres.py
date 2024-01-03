# Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.
palavraUser = input().split()
lista5caracteres = []

for i in palavraUser:
    if len(i) > 5:
        lista5caracteres.append(i)

print(palavraUser)
print(lista5caracteres)
