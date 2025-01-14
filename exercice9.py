#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.
lista = []
parlist = []
imparlist = []

for i in range(1,21):
    num = int(input("Digite um numero: "))
    lista.append(num)

for item in lista:
    if item % 2 ==0:
        parlist.append(item)
    else:
        imparlist.append(item)

print("Lista digitada: " + str(lista))
print("Lista de números pares digitados: " + str(parlist))
print("Lista de números impares digitados: " + str(imparlist))


