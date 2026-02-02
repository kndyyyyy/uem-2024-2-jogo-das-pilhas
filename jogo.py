import random

from pilha import Pilha

def IdentificaVitoria(pilhas: list[Pilha]):
   
    for i in range(len(pilhas)):
        for stacks in pilhas[i].Elem:
            if all(y == pilhas[stacks].Elem[0] for y in pilhas[stacks].Elem):
                if True:
                    return print('\nParabens, voce ganhou!')
            else:
                MoveElementosPilha(pilhas)

def MoveElementosPilha(pilhas: list[Pilha]):
    
    mover = False
    while not mover:

        print('\nQual pilha voce quer remover o elemento do topo ?')
        pilha_origem = int(input('\nPilha: '))
        pilha_origem = pilha_origem - 1
        print('\nQual pilha voce quer adicionar o elemento removido?')
        pilha_destino = int(input('\nPilha: '))
        pilha_destino = pilha_destino - 1
        
        if pilhas[pilha_origem].PilhaVazia():
            print('\nJogada Invalida. Escolha novamente.')
            continue

        elif pilhas[pilha_destino].PilhaCheia():
            print('\nJogada Invalida. Escolha novamente.')
            continue

        elif not pilhas[pilha_origem].PilhaVazia() and (not pilhas[pilha_destino].PilhaCheia() and not pilhas[pilha_destino].PilhaVazia()):
            if pilhas[pilha_destino].ElementoDoTopo() != pilhas[pilha_origem].ElementoDoTopo():
                print('\nJogada Invalida. aaEscolha novamente.')
                continue
            else:
                valor_desempilhado = pilhas[pilha_origem].Desempilha()
                pilhas[pilha_destino].Empilha(valor_desempilhado)
                print(pilhas)
                IdentificaVitoria(pilhas)
        else:
            valor_desempilhado = pilhas[pilha_origem].Desempilha()
            pilhas[pilha_destino].Empilha(valor_desempilhado)
            print(pilhas)
            IdentificaVitoria(pilhas)

def IniciaJogo(pilhas: list[Pilha]):

    sair = False
    while not sair:
        print("\nDigite 1 para Iniciar o Jogo")
        print("\nDigite 2 para Sair do Jogo")
        escolha = input("\nEscolha uma opcao: ")

        if escolha == "1":
            print("\nEscolha uma dificuldade de 1 ate 7")
            diff = int((input("\nDificuldade: ")))
            listanumeros = []
            for num in range(1, diff + 1):
                listanumeros.extend([num] * 4)

            random.shuffle(listanumeros)

            if diff == 1:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)

            elif diff == 2:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)
                

            elif diff == 3:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)

            elif diff == 4:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)

            elif diff == 5:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)

            elif diff == 6:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)

            elif diff == 7:
                for i in range(diff + 2):

                    stack = Pilha()
                    stack.InicializaPilha()
                    pilhas.append(stack)

                    if len(listanumeros) != 0:
                        for i in range(4):
                            stack.Empilha(listanumeros.pop(0))

                print(pilhas)
                IdentificaVitoria(pilhas)

            elif escolha == "2":
                sair = True

            else:
                print("Opcao Invalida.")


def main():
    pilhas: list[Pilha] = []
    IniciaJogo(pilhas)


main()
