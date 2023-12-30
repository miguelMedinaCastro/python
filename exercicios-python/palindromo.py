#  Escreva um programa em python que leia um texto e diga se é ou não um palíndromo (ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função no python que trabalhe com strings.
# Exemplos: Ama, mirim, A grama é amarga.

phrase = input("Informe algo: ").lower()

if phrase == phrase[::-1]:
    print("palíndromo")
else:
    print("Não é palíndromo")

print(phrase)
print(phrase[::-1])
