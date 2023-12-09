import unZip as u

with open("bigText.txt", "r") as arq:
    text = arq.read()

newList = text.split(" ")
count = 0

dictionary = {}
zipList = []

txtZip = ""

for word in newList:
    if word not in dictionary:
        dictionary[word] = str(count)
        txtZip += f'{word}: {dictionary[word]} '
        count += 1
    zipList.append(dictionary[word])


txtZip += '\n'
txtZip += '$ '
txtZip += " ".join(zipList)


with open("bigTextZip.txt", "w") as arq:
    arq.write(txtZip)

u.unZip()