#Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = []
lista2 = []
lista3 = []

print("Primeira lista")
for i in range(1,11):
    lista1.append(int(input("Digite um numero: ")))
print("Segunda lista")
for i in range(1,11):
    lista2.append(int(input("Digite um numero: ")))

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print("Vetor intercalado: " + str(lista3))