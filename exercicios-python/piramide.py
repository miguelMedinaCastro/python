#Crie um programa em Python que imprima uma sequência de números em forma de pirâmide. O programa deve solicitar ao usuário um número inteiro positivo e, em seguida, imprimir os números de 1 até o número informado, em linhas crescentes e decrescentes, formando uma pirâmide.

num = int(input("Digite um número inteiro positivo: "))
count = 1     
seq = str(count)
seq_rev = str(num) 

while num >= count: 
    print(seq) 
    count += 1 
    seq += str(count) 

rev = seq[::-1] 

count = 1 
while num >= count:
    print(rev[count:]) 
    count += 1 
