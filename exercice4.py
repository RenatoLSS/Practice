#Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

popA = 80000
popB = 200000
txA = 3
txB = 1.5
ano = 0

while popA <= popB:
    popA += (popA * (txA/100))
    popB += (popB * (txB/100))
    ano += 1

print(ano)