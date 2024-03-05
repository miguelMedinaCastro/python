# Crie duas matrizes 2x2 e realize a soma das duas matrizes. Imprima a matriz resultante.

matrizA = []


print("Matriz A:")

for i in range(2): 
    linhaA = []
    for j in range(2): 
        valorA = int(input(f"Informe valores numéricos para as posições ({i + 1}, {j + 1}): "))
        linhaA.append(valorA) 
    matrizA.append(linhaA)

print("Matriz B:")

matrizB = []
for k in range(2):
    linhaB = []
    for l in range(2):
        valorB = int(input(f"Informe valores numéricos para as posições ({k + 1}, {l + 1}): "))
        linhaB.append(valorB)
    matrizB.append(linhaB)

#adição entre as matrizes A e B:

matrizC = []

for m in range(2):
    linhaC = []
    for n in range(2):
        add = matrizA[m][n] + matrizB[m][n] 
        linhaC.append(add)    
    matrizC.append(linhaC)

for linha in matrizC:
    print(linha)
