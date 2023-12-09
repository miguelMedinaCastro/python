def unZip():
    with open("bigTextZip.txt", "r") as arq:
        zipText = arq.read()

    newList = zipText.split(" ")

    dictionary = {}
    dicList = []
    numberList = []

    cont = 0

    #ocorre a separação do texto zipado em 2
    while newList[cont] != "\n$": 
        dicList.append(newList[cont]) 
        cont += 1

    for i in range(cont + 1, len(newList)):
        numberList.append(newList[i])


    for j in range(0,len(dicList), 2):
        key = dicList[j]
        key = key[:-1]  #eliminação dos ":"
        value = dicList[j + 1]
        if key not in dictionary:
            dictionary[key] = str(value)

    new = []

    for i in newList:
        for key, value in dictionary.items():
            if i == value:
                new.append(key)

    newUnZip = " ".join(new)

    with open("unZip.txt", "w") as arq:
        arq.write(newUnZip)
