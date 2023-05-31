"""faça um programa que calcule a média aritmética de n notas.
n equivale ao total de avaliaçoes"""

n = int(input("Digite o total de avaliações: "))

soma = 0
contador = 0

while contador < n:
    nota = float(input("Digite a nota: "))
    soma += nota
    contador += 1

media = soma / n
print("A média aritmética das notas é:", media)
