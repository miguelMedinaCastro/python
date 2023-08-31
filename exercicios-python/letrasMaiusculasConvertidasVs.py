# Escreva um programa que recebe uma string do usuário e imprime a string com todas as letras maiúsculas convertidas para minúsculas e vice-versa.

phrase = input("Informe uma frase: ")
new_phrase = ""
for letter in phrase:
    if ord("A") <= ord(letter) <= ord("Z"):
        code = ord(letter) + 32
        caractere = chr(code)
        new_phrase += caractere
    else:
        new_phrase += letter
print(new_phrase)
