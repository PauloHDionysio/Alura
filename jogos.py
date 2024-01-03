import adivinhacao
import teste

print("Qual jogo ira jogar?", end = '\n')
opcao = int(input("(1) - Adivinhacao (2) - Teste"))
if(opcao == 1):
    print("Voce escolheu ADIVINHACAO")
    adivinhacao.jogar()
elif(opcao == 2):
    print("Voce escolheu TESTE")
    teste.jogar()