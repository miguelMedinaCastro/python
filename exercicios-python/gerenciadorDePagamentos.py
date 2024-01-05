print(("=" * 10), "LOJA", ("=" * 10))

price = float(input("Preço das compras: R$"))

menu = True

while menu:
    print("[ 1 ] à vista dinheiro/cheque")
    print("[ 2 ] à vista cartão")
    print("[ 3 ] 2x no cartão")
    print("[ 4 ] 3x ou mais no cartão")
    choice = int(input("Qual é a opção? "))

    if choice == 1:
        discount = ((price / 100) * 10)
        print(f"Sua compra de R${price} vai custar R${price - discount} no final.")
        menu = False
    elif choice == 2:
        discount = ((price / 100) * 5)
        print(f"Sua compra de R${price} vai custar R${price - discount} no final.")
        menu = False
    elif choice == 3:
        portion = price / 2
        print(f"Sua compra será parcelada em 2x de R${portion} SEM JUROS.")
        print(f"Sua compra de R${price} irá custar os mesmos R${price} no final.")
        menu = False
    elif choice == 4:
        portion = int(input("Quantas parcelas? "))
        if portion < 3:
            print("Inválido, tente novamente.")
        else:
            moneyRent = ((price / portion) / 100) * 20
            bank = moneyRent + (price / portion)
            fullPrice = price + price / 100 * 20 
            print(f"Sua compra será parcelada em {portion}x de R${bank} COM JUROS")
            print(f"Sua compra de R${price} vai custar R${fullPrice} no final.")
            menu = False
    else:
        print("Volte sempre :)")
        menu = False

