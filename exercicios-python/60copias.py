#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

book = 24.95
discount = (book / 100) * 40 
equal = book - discount

examples = 59 * 0.75 
value = ((equal + 3) * examples) 

print(f"custo: R${value:.2f}")
