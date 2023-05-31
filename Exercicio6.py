"""  Escrever um algoritmo que lê o número de identificação, as 3 notas passadas por um aluno
 nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de
 aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
A consideração de conceitos obedece a tabela abaixo:

Média de Aproveitamento | conceito
MA >= 9,0               | A
7,5 <= MA < 9,0         | B
6,0 <= MA < 7,5         | C
4,0 <= MA < 6,0         | D
AM < 4,0                | E

O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, 
o conceito correspondente à mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E.
 Pergunte se o usuário deseja digitar as notas de outro aluno S para sim e N para não"""

continuar = True

while continuar:
    num_identificacao = input("Digite o número de identificação do aluno: ")
    nota1 = float(input("Digite a primeira nota (entre 0 e 10): "))
    nota2 = float(input("Digite a segunda nota (entre 0 e 10): "))
    nota3 = float(input("Digite a terceira nota (entre 0 e 10): "))
    me = float(input("Digite a nota dos exercícios (entre 0 e 10): "))

    ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7

    if ma >= 9.0:
        conceito = "A"
    elif ma >= 7.5:
        conceito = "B"
    elif ma >= 6.0:
        conceito = "C"
    elif ma >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

    print("\nNúmero de identificação:", num_identificacao)
    print("Notas:", nota1, nota2, nota3)
    print("Média dos exercícios:", me)
    print("Média de aproveitamento:", ma)
    print("Conceito:", conceito)

    if conceito in ["A", "B", "C"]:
        print("APROVADO\n")
    else:
        print("REPROVADO\n")

    resposta = input("Deseja digitar as notas de outro aluno? (S/N): ")
    if resposta.upper() != "S":
        continuar = False
