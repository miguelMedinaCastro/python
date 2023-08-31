#Crie um programa em Python que imprima uma sequência de números em forma de pirâmide. O programa deve solicitar ao usuário um número inteiro positivo e, em seguida, imprimir os números de 1 até o número informado, em linhas crescentes e decrescentes, formando uma pirâmide.
num = int(input("Digite um número inteiro positivo: "))
count = 1     # count começa no 1
seq = str(count) # seq faz o count virar string
seq_rev = str(num) # seq reversa

while num >= count: # enquanto num for maior ou igual à count
    print(seq) # vai printar a seq, no caso '1'
    count += 1 # count passa de 1 para 2
    seq += str(count) # e o count = 2 é adicionado na seq, assim o processo se repete sempre aumentando de 1 em 1 até chegar o valor que o user digitou

rev = seq[::-1] # inverteu a string, então por exemplo(1234, fica 54321)

count = 1 # count volta a ser 1 novamente
while num >= count:
    print(rev[count:]) # isso elimina o num 5
    count += 1 # count passa de 1 para 2
