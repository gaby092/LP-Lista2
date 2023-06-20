""" Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” 
e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade."""

def verificar_idade():
    for i in range(1, 76):
        idade = int(input(f"Informe a idade da pessoa {i}: "))
        if idade >= 18:
            print(f"A pessoa {i} é maior de idade.")
        else:
            print(f"A pessoa {i} é menor de idade.")

verificar_idade()
