# ********************************* ANOTACOES ***********************************

# .find() -> Devolve a posicao da letra na string.
# .count(x) -> Devolve o numero de vezes que 'x' foi repetido
# .index() -> Retorna o índice da primeira ocorrência de um determinado elemento em uma lista

# set() -> não é uma lista pois não tem indice, no entando armazena em uma lista e não aceita valores repetidos

# "acertou = "_" not in letras_acertadas" -> Verifica se o caractere "_" não está presente na lista letras_acertadas.

# .strip() -> apaga os espacos existentes e caracteres especiais e deixa apenas os caracteres

# *******************************************************************************
import random

def jogar():
    apresentacao()

    palavra_secreta = leitura_do_arquivo()

    letra_acertadas = palavra_acertadas(palavra_secreta)

    enforcar = False
    acertou = False
    tentativas = 0

    # enquanto NAO ENFORCOU E  NAO ACERTOU || para sair do looping os dois devem ser verdadeiros
    while(not enforcar and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letra_acertadas, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        print(tentativas)
        enforcar = tentativas == 7
        acertou = "_" not in letra_acertadas
        print(letra_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(count):
    print("  _______     ")
    print(" |/      |    ")

    if (count == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (count == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (count == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (count == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (count == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (count == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (count == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def apresentacao():
    print("**************************************")
    print("***** Bem vindo ao jogo da Forca *****")
    print("**************************************")

def marca_chute_correto(chute, letra_acertadas, palavra_secreta):
    count = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letra_acertadas[count] = letra
        count += 1
    return count

def leitura_do_arquivo():
    arquivo = open('frutas.txt', 'r')
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def palavra_acertadas(palavra_secreta):
    #                  "_" para cada letra na palavra secreta
    letra_acertadas = ["_" for letra in palavra_secreta]
    return letra_acertadas


if(__name__ == "__main__"):
    jogar()