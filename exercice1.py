#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

nota = float(input("Informe a nota do aluno: "))
while nota > 10 or nota < 0:
    print("Valor invalido")
    nota = float(input("Informe a nota do aluno: "))

print("Valor aceito: " + str(nota))



