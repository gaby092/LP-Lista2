"""Faça um programa que leia um nome de usuário 
e sua senha e não aceite a senha igual ao nome 
do usuário, mostrando uma mensagem de erro e 
retornando a pedir as informações."""

while True:
    usuario = input('digite o nome de usuario: ')
    senha= input('digite sua senha: ')
    if usuario != senha:
       break
    else:
        print(f'erro, insira uma senha valida.')
print(f'bem vindo')