#Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random

menu = True

while menu:

    print("Suas opções:")
    print("[ 0 ] PEDRA")
    print("[ 1 ] PAPEL")
    print("[ 2 ] TESOURA")
    player = int(input("Qual é a sua jogada? "))

    pc = random.randint(0, 2)

    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO!!!")

    if player == 0 and pc == 1:
        print("-=" * 20)
        print("Computador jogou Papel")
        print("Jogador jogou Pedra")
        print("-=" * 20)
        print("COMPUTADOR VENCE")
        menu = False
    elif player == 1 and pc == 0:
        print("-=" * 20)
        print("Computador jogou Pedra")
        print("Jogador jogou Papel")
        print("-=" * 20)
        print("JOGADOR VENCE")
        menu = False
    elif player == 2 and pc == 1:
        print("-=" * 20)
        print("Computador jogou Papel")
        print("Jogador jogou Tesoura")
        print("-=" * 20)
        print("JOGADOR VENCE")
        menu = False
    elif player == 1 and pc == 2:
        print("-=" * 20)
        print("Computador jogou Tesoura")
        print("Jogador jogou Papel")
        print("-=" * 20)
        print("COMPUTADOR VENCE")
        menu = False
    elif player == 0 and pc == 2:
        print("-=" * 20)
        print("Computador jogou Tesoura")
        print("Jogador jogou Pedra")
        print("-=" * 20)
        print("JOGADOR VENCE")
        menu = False
    elif player == 2 and pc == 0:
        print("-=" * 20)
        print("Computador jogou Pedra")
        print("Jogador jogou Tesoura")
        print("-=" * 20)
        print("COMPUTADOR VENCE")
        menu = False
    elif player == 0 and pc == 0:
        print("-=" * 20)
        print("Computador jogou Pedra")
        print("Jogador jogou Pedra")
        print("-=" * 20)
        print("EMPATE")
        menu = False
    elif player == 1 and pc == 1:
        print("-=" * 20)
        print("Computador jogou Papel")
        print("Jogador jogou Papel")
        print("-=" * 20)
        print("EMPATE")
        menu = False
    elif player == 2 and pc == 2:
        print("-=" * 20)
        print("Computador jogou Tesoura")
        print("Jogador jogou Tesoura")
        print("-=" * 20)
        print("EMPATE")
        menu = False

