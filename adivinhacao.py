# ******************************************************************************************************************************
# AREA DE ANOTAÇÕES
# Algumas funcoes ja estao embutidas no python. Algumas outras funcoes nao, como por exemplo, a funcao RANDOM().
# random() -> numeros aleatorios. Necessario IMPORTACAO || 'import random' 'random.random()'

# round() -> funcao para arredondar um numero com casa decimais

# random.randrange() -> retorna um valor de 1(incluso) a 101(nao incluso)

# abs() -> funcao que devolve o valor absoluto. abs(-90) = 90, abs(90) = 90

# ******************************************************************************************************************************
import random

def jogar():
    secret_number = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Escolha um nivel")
    print("(1) Facil (2) Medio (3) Dificil")
    nivel = int(input("Nivel: "))

    if(nivel == 1):
        tentativas = 15
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):

        print("rodada {} de {}".format(rodada, tentativas))

        # limitando um valor para o input
        chute_str = input()
        chute = int(chute_str)

        # continue pula para a proxima interacao sem sair do laço
        if (chute < 1 or chute > 100):
            print("Nao pode haver valores menores que 1")
            continue

        acertou = chute == secret_number
        maior = chute > secret_number
        menor = chute < secret_number

        if(acertou):
            print("Voce acertou! Na rodada {} obteve a resposta correta. PONTOS: {}".format(rodada, pontos))
            print("O numero CORRETO eh: ", secret_number)
            break
        elif (maior):
            print("Errado! Valor MAIOR que o numero correto")
            # Calculo para definir o valor de pontos perdidos e total de ponto no final do jogo
            pontos_perdidos = abs(secret_number - chute)
            pontos -= pontos_perdidos
        elif (menor):
            print("Errado! Valor MENOR que o numero correto")
            # Calculo para definir o valor de pontos perdidos e total de ponto no final do jogo
            pontos_perdidos = abs(secret_number - chute)
            pontos -= pontos_perdidos


    print("Finalizado! O numero era {}".format(secret_number))

if(__name__ == "__main__"):
    jogar()