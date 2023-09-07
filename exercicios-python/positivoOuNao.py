# Faça um programa que leia um número inteiro e verifique se ele é positivo, negativo ou zero. Imprima uma mensagem adequada para cada caso.

num = int(input("Informe um número: "))

if num > 0:
	print("Positivo")
elif num == 0:
	print("Zero")
else:
	print("Negativo")
