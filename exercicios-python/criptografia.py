cT = int(input())

encrypted = []

for _ in range(cT):
    string = input("Informe a string: ")

    newString = ""
    middleChanged = ""

    for i in string:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            newString += chr(ord(i) + 3)
        elif ord(i) == 32:
            newString += chr(ord(i))
        else:
            newString += i

    reverseString = newString[::-1]
    half = len(reverseString) // 2
    separateStringOne = reverseString[:half]
    separateStringTwo = reverseString[half:]

    for j in separateStringTwo:
        middleChanged += chr(ord(j) - 1)
        final = separateStringOne + middleChanged

    encrypted.append(final)

print(encrypted)    
