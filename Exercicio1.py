"""Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido."""

while True:
    n = float(input("Digite uma nota entre zero e dez: "))
    if n >= 0 and  n <= 10:
        break
    else:
        print("Valor inválido. Digite novamente.")

print("Valor válido inserido:", n )