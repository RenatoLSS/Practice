#Faça um programa que leia 5 números e informe o maior número.

lista = []

for i in range(1,6):
    num = int(input("Digite um numero: "))
    lista.append(num)

maior = max(lista)
print("Maior numero digitado: " + str(maior))