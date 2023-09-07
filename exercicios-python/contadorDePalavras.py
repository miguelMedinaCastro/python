# Escreva um programa que recebe uma frase do usuário e conta o número de palavras na frase.

phrase = input("Informe uma frase: ")
count = 1
for word in phrase: 
    if word == " ":
        count += 1
print(count)
