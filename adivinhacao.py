import random
import time

print("===================")
print("JOGO DE ADIVINHAÇÃO")
print("===================")



def ilimitado():
    while True:
        try:
            print("ESCOLHA O NÚMERO MÁXIMO QUE A MÁQUINA PODERÁ ESCOLHER!")
            x = int(input("-> "))
            escolha = random.randint(1, x)
            tentativas = 0
            print(f"ESCOLHA UM NÚMERO ENTRE 1 á {x}")
            jogador = int(input(">"))
            if escolha == jogador:
                print("NÚMERO CORRETO!")
                print(f"VOCÊ ACERTOU COM {tentativas} TENTATIVAS")
                break

            elif escolha > jogador:
                print("O NÚMERO ESCOLHIDO É MAIOR!")
                tentativas += 1
                ilimitado()

            elif escolha < jogador:
                print("O NÚMERO É MENOR!")
                tentativas += 1
                ilimitado()

            elif jogador > x:
                print("INSIRA UM NÚMERO MENOR QUE O NÚMERO MÁXIMO!")
                ilimitado()
        except ValueError:
            print("INCORRETO!")

# LIMITADO
def limitado():
    print("ESCOLHA O NÚMERO MÁXIMO QUE A MÁQUINA PODERÁ ESCOLHER!")
    x = int(input("-> "))
    print("ESCOLHA O MÁXIMO DE TENTATIVAS QUE VOCÊ PODERÁ FAZER!")
    y = int(input("-> "))
    print(f"ESCOLHA UM NÚMERO ENTRE 1 Á {x}")
    escolha = random.randint(1, x)
    tentativas = 0
    try:

        while tentativas < y:
            jogador = int(input("-> "))

            # SE O NÚMERO FOR ACERTADO!
            if jogador == escolha:
                print("VOCÊ ACERTOU O NÚMERO CORRETO!")
                print(f"VOCÊ ACERTOU COM {tentativas} de {y} TENTATIVAS")
                break

            # SE O NÚMERO FOR MAIOR
            elif jogador < escolha:
                print("O NÚMERO ESCOLHIDO É MAIOR!")
                tentativas += 1
                print(f"VOCÊ TEM {y - tentativas} TENTATIVAS RESTANTE!")
                time.sleep(0.5)
                if tentativas == y:
                    print(f"VOCÊ PERDEU, O NÚMERO ERA {escolha}")
                    print(f"O NÚMERO MÁXIMO {tentativas} DE TENTATIVAS FOI ALCANÇADO!")
                else:
                    print("COLOQUE O NÚMERO CORRETO!")

            # SE O NÚMERO FOR MENOR.
            elif jogador > escolha:
                print("O NÚMERO ESCOLHIDO É MENOR!")
                tentativas += 1
                print(f"VOCÊ TEM {y - tentativas} TENTATIVAS RESTANTE!")
                time.sleep(0.5)
                if tentativas == y:
                    time.sleep(1)
                    print(f"VOCÊ PERDEU, O NÚMERO ERA {escolha}")
                    print(f"O NÚMERO MÁXIMO {tentativas} DE TENTATIVAS FOI ALCANÇADO!")
                elif jogador > x:
                    print("INSIRA UM NÚMERO MENOR QUE O NÚMERO MÁXIMO!")
                    limitado()

    except ValueError:
        print("INCORRETO!")

def modo_de_jogo():
    print("""
    EXISTEM DUAS OPÇÕES DE JOGO:
    [1] - MODO DE TENTATIVAS ILIMITADAS, VOCÊ NÃO TERÁ UM LIMITE DE QUANTAS VEZES TENTAR ACERTAR O NÚMERO CORRETO!
    [2] - MODO DE TENTATIVAS LIMITADA, VOCÊ ESCOLHERÁ O LIMITE DE TENTATIVAS PARA VOCÊ ACERTAR O NÚMERO CORRETO!
    """)
    jogo = input("-> ")
    time.sleep(0.5)

    if jogo == "1":
        ilimitado()

    elif jogo == "2":
        limitado()

    # GARANTIR QUE O NÚMERO SEJA 1 OU 2
    else:
        print(f"VOCÊ ESCOLHEU UMA ALTERNATIVA INEXISTENTE {jogo}")
        modo_de_jogo()

modo_de_jogo()

def novamente():
    print("DESEJA NOVAMENTE JOGAR?")
    print("""
    CASO A RESPOSTA FOR SIM DIGITE 1.
    """)
    nov = int(input("-> "))
    if nov == 1:
        print("""
        ESCOLHA UM DOS DOIS MODOS DE JOGOS.
        [1] - MODO ILIMITADO
        [2] - MODO LIMITADO
        """)
        novescolha()
    else:
        print("JOGO ENCERRADO!")
def novescolha():
    nov2 = int(input("-> "))
    if nov2 == 1:
        ilimitado()
    elif nov2 == 2:
        limitado()

novamente()