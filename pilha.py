#Variavel responsavel por fixar o tamanho maximo da pilha
TAM_MAX = 4

from dataclasses import dataclass

#dataclass implementando como sendo um tipo pilha
@dataclass
class Pilha:

    def __init__(P):
        P.Topo = -1
        P.Elem = []

    def InicializaPilha(P):
    #Funcao responsavel por inicializar a pilha
        P.Topo = -1
        P.Elem = [0]*TAM_MAX

    def PilhaVazia(P):
    #Funcao responsavel pela verificacao se a pilha esta vazia
        return P.Topo == -1
    
    def PilhaCheia(P):
    #Funcao responsavel pela verificacao se a pilha esta cheia
        return P.Topo == TAM_MAX - 1
    
    def Empilha(P, x:int):
    #Funcao responsavel por empilhar a pilha
        if not P.PilhaCheia():
            P.Topo = P.Topo + 1
            P.Elem[P.Topo] = x
        else:
            print('\nA pilha esta cheia')

    def Desempilha(P):
    #Funcao responsavel por desempilhar a pilha
        if not P.PilhaVazia():
            x = P.Elem[P.Topo]
            P.Elem[P.Topo] = 0
            P.Topo = P.Topo - 1
            return x

    def ElementoDoTopo(P):
    #Funcao que retorna qual e o atual elemento do topo
        if not P.PilhaVazia():
            return P.Elem[P.Topo]
        else:
            print("A Pilha esta vazia")


    def __repr__(P) -> str:
        content = "["
        for value in P.Elem:
            if value == 0:
                break
            content += f"{value},"
        if len(content) == 1:
            return "[]"
        return content[:-1] + "]"
    
    #def __repr__(P) -> str:
        #return f"{P.Elem}"

