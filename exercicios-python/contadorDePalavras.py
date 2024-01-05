phrase = input("Informe uma frase: ")
count = 1
for word in phrase: 
    if word == " ":
        count += 1
print(count)
