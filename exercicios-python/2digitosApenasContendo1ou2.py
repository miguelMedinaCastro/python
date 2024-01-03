# mostrar apenas números contendo 2 dígitos, múltiplos por 3 que tenham apenas os dígitos 1 ou 2.
for i in range(10, 100):
    if i % 3 == 0:
        if "1" in str(i) or "2" in str(i):
            print(i)
            
