"""Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número
"""

def verificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

# Solicitar a quantidade de números
quantidade = int(input("Digite a quantidade de números a serem verificados: "))

# Loop para receber os números e mostrar o resultado
for i in range(quantidade):
    numero = float(input("Digite um número: "))
    resultado = verificar_numero(numero)
    print(f"O número {numero} é {resultado}.")
