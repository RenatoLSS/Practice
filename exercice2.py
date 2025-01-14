#Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("Favor digitar nome de usuário: ")
passw = input("Favor digitar senha: ")

while user == passw:
    print("Não é aceitavel senha igual ao nome de usuário")
    user = input("Favor digitar nome de usuário: ")
    passw = input("Favor digitar senha: ")

print("Cadastro realizado")