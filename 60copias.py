#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

book = 24.95
discount = (book / 100) * 40 #porcentagem de 40% de desconto do livro
equal = book - discount #diferença do preço com a porcentagem

examples = 59 * 0.75 #calculando o custo de todas as demais cópias adicionais
value = ((equal + 3) * examples) #equal + 3 para somar a única cópia que vale 3 multiplicando com examples 

print(f"custo: R${value:.2f}")
