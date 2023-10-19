# Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.

user = input("Digite uma frase: ").lower() 
listUser = user.split() 
newList = [] 
for word in listUser:
    if len(word) > 5:
        newList.append(word) 
print(newList) 
