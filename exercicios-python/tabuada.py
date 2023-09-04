# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada (de 0 a 10).

num = int(input("Informe um número: "))

for n in range(0, 11):
    print("{} x {} = {}".format(num, n, num * n))
