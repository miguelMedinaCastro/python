# Crie duas matrizes 2x2 e realize a soma das duas matrizes. Imprima a matriz resultante.

matrizA = []

#criação das matrizes 2 x 2 feita pelo usuário:

print("Matriz A:")

for i in range(2): #limitar range em 2
    linhaA = []
    for j in range(2): #limitar range em 2, assim, i e j formam uma matriz quadrada, ou seja, i = j
        valorA = int(input(f"Informe valores numéricos para as posições ({i + 1}, {j + 1}): ")) #usuario informa por posições já pré estabelecidas os valores numéricos, obs: "+ 1" para não começar com 0
        linhaA.append(valorA) #i(linha) adicionados na lista vazia
    matrizA.append(linhaA) #j(coluna) adicionados na lista vazia

print("Matriz B:")

matrizB = []
#exatamente o mesmo processo da matriz A.
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
        add = matrizA[m][n] + matrizB[m][n] #novas variáveis para representar i,j,k e l, ocorre a soma por posição
        linhaC.append(add)    
    matrizC.append(linhaC)
#representação de uma matriz: 
for linha in matrizC:
    print(linha)
