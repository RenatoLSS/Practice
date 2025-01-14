#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo.
# Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos.
# Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação python.
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
# Um número de jogador igual zero, indica que a votação foi encerrada.
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
# Após o final da votação, o programa deverá exibir:

#O total de votos computados;
#Os números e respectivos votos de todos os jogadores que receberam votos;
#O percentual de votos de cada um destes jogadores;
#O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo n
# o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
# A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo.
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco,
# obedecendo a mesma disposição apresentada na tela.

#Enquete: Quem foi o melhor jogador?

#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 11
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 50
#Informe um valor entre 1 e 23 ou 0 para sair!
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 0

#Resultado da votação:

#Foram computados 8 votos.

#Jogador Votos           %
#9               4               50,0%
#10              3               37,5%
#11              1               12,5%
#O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

mvp = [] #Lista para gravar votors
camisa = 1#inicialização da variavel

print("Enquete: Quem foi o melhor jogador? ")

while camisa != 0: #loop para continuar solicitando numeros até condição de parada
    camisa = int(input("Número do jogador (0=fim): "))
    if camisa>23 or camisa<0:#condição para verificar se numero é valido
        camisa = int(input("Informe um valor entre 1 e 23 ou 0 para sair!"))
    if camisa != 0:
        mvp.append(camisa)#gravar na lista caso o valor seja valido e firente de 0

print(" Foram computados " + str(len(mvp)) + " votos")
print("")
print(" Resultado da votação ")
print("")
print(" Jogador   Votos    %")

melhorjogador = 1
frequencia = {} #dicionario para gravar numeros e quantidade de vezes que aparece
for i in mvp: #loop para percorrer a lista de votos
    if i in frequencia:#condicional para verificar se o numero já existe na lista de frequencia
        frequencia[i] += 1#se existe acrescenta um voto
    else:
        frequencia[i] = 1#senão adiciona um voto

total = len(mvp) #total de votos
for numero, contagem in sorted(frequencia.items(), key=lambda item: item[1], reverse=True):#impressão do dicionario ordenado pela quantidade de votos
    print(str(numero) + "        " + str(contagem) + "         " + str((contagem/total)*100) +"%")

#variáveis para armazenar o melhor jogador e seus votos
melhor_jogador = None
max_votos = 0

for numero, contagem in frequencia.items():#loop para identificar o jogador com mais votos
    if contagem > max_votos:
        melhor_jogador = numero
        max_votos = contagem

percentual_mvp = (max_votos / total) * 100#cálculo do percentual do melhor jogador

#exibição do melhor jogador e seus detalhes
print("\nO melhor jogador foi o número " + str(melhor_jogador) + ", com " + str(max_votos) + " votos, correspondendo a " + str(round(percentual_mvp, 2)) + "% do total de votos.")


