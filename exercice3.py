#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o nome: ")

while len(nome)< 3:
    print("Não é aceitavel nome com menos de 3 letras")
    nome = input("Digite o nome: ")

idade = int(input("Digite a idade:"))
while idade>150 or idade<0:
    print("Não é aceitavel idade inferior a 0 ou superior a 150 anos.")
    idade = int(input("Digite a idade:"))

salario = float(input("Digite o salario: "))
while salario <= 0:
    print("Não é aceitavel salario inferior a 0.")
    salario = float(input("Digite o salario: "))

sexo = input("Digite o sexo: (M) (F)")
actsexo = ('m','f')
while sexo not in actsexo:
    print("Valor de sexo incorreto, favor digitar M para masculino ou F para feminino")
    sexo = input("Digite o sexo: (M) (F)")

estc = input("Digite o estado civil: (S)solteiro(a), (C)casado(a), (V)viuvo(a), (D)divorciado(a)")
vlr = ('s', 'c', 'v', 'd')
while estc not in vlr:
    print("O valor não é permitido")
    estc = input("Digite o estado civil: (S)solteiro(a), (C)casado(a), (V)viuvo(a), (D)divorciado(a): ")

print("Cadastro realizado")
print("Nome: "+nome)
print("Idade: " + str(idade))
print("Salario: " + str(salario))
if(sexo == 'm'):
    print("Sexo: Masculino")
else:
    print("Sexo: Feminino")

if(estc == 's'):
    print("Estado civil: Solteiro(a)")
elif(estc=='c'):
    print("Estado civil: Casado(a)")
elif (estc == 'v'):
    print("Estado civil: Viúvo(a)")
elif (estc == 'd'):
    print("Estado civil: Divorciado(a)")