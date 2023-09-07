#Crie um programa que recebe uma string com letras maiusculas, espaços e números como entrada e retorna uma nova string em que cada caractere foi convertido para o código Morse.

#Código Morse:

#Exemplo:

#Informe a mensagem: HELLO 123

#Saída esperada: ".... . .-.. .-.. ---   .---- ..--- ...--"

string = input("Informe a mensagem: ").strip().upper()

newString = [] #lista vazia

morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"] #código morse de A até Z(incluindo os de números de 0 a 9)

#i vai percorrer letra por letra na string:
for i in string: 
    if 65 <= ord(i) <= 90: #se o i for maior ou igual ao código ASCII de A e ASCII de Z 
        position = ord(i) - 65 #pega código ASCII do i(letra em questão) e realiza uma subtração de 65(ASCII do A)
        newString.append(morseCode[position]) #assim, se pega a posição do A na lista, do B, C, D, .... até Z
    #se tiver espaço na string:
    elif " " in i: 
        newString.append(" ") #apenas se adiciona um espaço, simples assim
    #se o i não está entre letras:
    else: 
        if 48 <= ord(i) <= 57: #se o i for maior ou igual ao ASCII de 0 e ASCII de 9
            position = (ord(i) - 48) + 25 #pega código ASCII do i(número em questão) e realiza uma subtração de 48(ASCII de 0) & depois fazer uma soma 25(para saber em qual posição está o número após o alfabeto)
            newString.append(morseCode[position]) #assim, se pega a posição do 0, 1, 2, ... até 9

removeOne = "".join(str(newString).strip("[]")) #para retirar os colchetes
removeTwo = removeOne.replace(",", "") #para retirar as vírgulas
removeThree = removeTwo.replace("'", "") #para retirar as aspas

print("Saída esperada:", removeThree) #printa e voilá
