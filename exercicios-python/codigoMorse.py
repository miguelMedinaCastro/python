string = input("Informe a mensagem: ").strip().upper()

newString = [] #lista vazia

morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"] #código morse de A até Z(incluindo os de números de 0 a 9)

for i in string: 
    if 65 <= ord(i) <= 90: 
        position = ord(i) - 65 
        newString.append(morseCode[position])
    elif " " in i: 
        newString.append(" ") 
    else: 
        if 48 <= ord(i) <= 57: 
            position = (ord(i) - 48) + 25 #realiza uma subtração de 48(ASCII de 0) & depois fazer + 25(para saber em qual posição está o número após o alfabeto)
            newString.append(morseCode[position]) #assim, se pega a posição do 0, 1, 2, ... até 9

removeOne = "".join(str(newString).strip("[]")) 
removeTwo = removeOne.replace(",", "") 
removeThree = removeTwo.replace("'", "") 

print("Saída esperada:", removeThree) 
