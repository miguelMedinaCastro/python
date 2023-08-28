# Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.

user = input("Digite uma frase: ").lower() #input do user
listUser = user.split() #função '.split()' para a str(user) virar uma list
newList = [] #vazia, reservada para armazenar as palavras com mais de 5 caracteres

for word in listUser: #word vai percorrer a listUser
    if len(word) > 5: #se o tamanho de word(palavra) for maior do que 5
        newList.append(word) #então a palavra é adicionada a newList
print(newList) #print newList