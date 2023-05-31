"""Ler 80 números e ao final informar quantos número(s) estão(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive)."""

contador = 0
n = 0

while contador < 80:
    numero = int(input("Digite um número: "))
    contador += 1

    if 10 <= numero <= 150:
        n += 1

print(f'Total de números {n}')
    