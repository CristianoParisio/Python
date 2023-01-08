qtd = 0
soma = 0
media = 0
valor = 0

valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    
    valor = float(input("Digite um valor: "))
    
media = soma / qtd
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média de valores: ", media)

# esse WHILE enquanto valor for maior que zero ele vai
# somar os valores e qdo digitar o ou -1 que é a condição
# while o programa vai fazer a média de todos os valores
# digitados mais qde de valores digitados