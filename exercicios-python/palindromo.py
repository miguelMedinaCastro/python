phrase = input("Informe algo: ").lower()

if phrase == phrase[::-1]:
    print("palíndromo")
else:
    print("Não é palíndromo")

print(phrase)
print(phrase[::-1])
