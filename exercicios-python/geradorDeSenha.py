import random #módulo importante para decisão randômica disponível no próprio python

lower = "abcdefghijklmnopqrstuvwxyz" #string com os alfabetos todos minúsculos 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #string com os alfabetos todos em maiúsculos
special = "!@#$%*()[]{}\|,.;:?/°º=-_+'" #string com os caracteres especiais
num = "0123456789" #string com números

all = lower + upper + special + num #concatenação com as 4 variáveis
length = 20 #tamanho da senha
password = "".join(random.sample(all, length)) #password é uma string vazia, '.join()' irá acrescentar em password elementos aleatórios graças a função 'random.sample(var, var determinante)'

print(password) #print password
