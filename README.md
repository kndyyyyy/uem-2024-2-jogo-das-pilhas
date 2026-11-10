# Jogo das Pilhas (Python)

Versão original em Python do trabalho **Jogo das Pilhas**.
O jogo é executado no terminal e o objetivo é reorganizar os números até que
cada pilha fique vazia ou completa com quatro números iguais.

## Como executar

### Pré-requisitos

- Python 3 instalado

### Rodando o projeto

```bash
python3 jogo.py
```

Em alguns sistemas, o comando pode ser:

```bash
python jogo.py
```

## Como jogar

1. Escolha a opção `1` no menu para iniciar.
2. Escolha uma dificuldade de `1` a `7`.
3. Informe o número da pilha de origem (de onde o elemento do topo será
   removido).
4. Informe o número da pilha de destino.
5. Repita as jogadas até organizar todas as pilhas.

### Regras

- Cada número aparece **4 vezes** no tabuleiro.
- A dificuldade define quantos números diferentes serão usados e quantas pilhas
  cheias existirão. São sempre acrescentadas **2 pilhas vazias**.
- Só é possível mover o elemento do **topo** de uma pilha.
- O destino deve ser uma pilha **vazia** ou uma pilha cujo **topo tenha o mesmo
  número**.
- Não é possível mover para uma pilha **cheia**.
- A vitória acontece quando todas as pilhas estão vazias ou completas com quatro
  números iguais.

## Exemplo de execução

```text
Digite 1 para Iniciar o Jogo

Digite 2 para Sair do Jogo

Escolha uma opcao: 1

Escolha uma dificuldade de 1 ate 7

Dificuldade: 2
[[2,1,2,1], [1,1,2,2], [], []]

Qual pilha voce quer remover o elemento do topo ?

Pilha: 2

Qual pilha voce quer adicionar o elemento removido?

Pilha: 3

[[2,1,2,1], [1,1,2], [2], []]
...
```

## Conceitos de Python utilizados

- Implementação manual de uma pilha com lista e índice `Topo`.
- Classe com `@dataclass`.
- Operações de pilha: empilhar, desempilhar, consultar o topo, verificar se está
  vazia e se está cheia.
- Listas dinâmicas e embaralhamento com `random.shuffle`.
- `__repr__` para representar a pilha.
- Entrada e saída com `input` e `print`.

## Observações

- Esta é a versão original do trabalho, escrita em Python.
- A versão em C# foi criada posteriormente e corrige alguns problemas de fluxo,
  validação de entrada e verificação de vitória.
