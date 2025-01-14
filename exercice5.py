#Altere o programa anterior permitindo ao usuário informar as populações e
# as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
popA = int(input("Digite a população do primeiro País: "))
popB = int(input("Digite a população do segundo País: "))
txA = float(input("Digite a taxa de crescimento do primeiro País: (%)"))
if txA >100 or txA<0:
    print("Valor invalido para porcentagem.")
    txA = float(input("Digite a taxa de crescimento do primeiro País: (%)"))
txB = float(input("Digite a taxa de crescimento do segundo País: (%)"))
if txB >100 or txB<0:
    print("Valor invalido para porcentagem.")
    txB = float(input("Digite a taxa de crescimento do primeiro País: (%)"))
ano = 0

while popA <= popB:
    popA += (popA * (txA/100))
    popB += (popB * (txB/100))
    ano += 1

print(ano)