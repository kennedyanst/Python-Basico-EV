qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma +=valor
    qtd += 1
    # Entrada de valores
    valor = float(input("Digite um valor: "))

# Caso digite um valor negativo o laço encerra
media = soma / qtd
print(f"Total de soma: {soma}")
print(f"Quantidade de valores digitados: {qtd}")
print(f"Média dos valores: {media}")
