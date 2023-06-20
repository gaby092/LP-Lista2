"""Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos.
 Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe a média de preço de custo e do preço de venda."""

 def calcular_lucro_prejuizo(custo, venda):
    if venda > custo:
        return "Lucro"
    elif venda < custo:
        return "Prejuízo"
    else:
        return "Empate"

# Inicializar as variáveis de soma
somacusto = 0
soma_venda = 0

# Loop para receber os preços de custo e venda
for i in range(1, 41):
    print(f"\nProduto {i}:")
    custo = float(input("Digite o preço de custo: "))
    venda = float(input("Digite o preço de venda: "))

    resultado = calcular_lucro_prejuizo(custo, venda)
    print(f"Resultado: {resultado}")

    somacusto += custo
    soma_venda += venda

# Calcular as médias
media_custo = somacusto / 40
media_venda = soma_venda / 40

# Exibir as médias
print("\nMédia de preço de custo:", media_custo)
print("Média de preço de venda:", media_venda)
