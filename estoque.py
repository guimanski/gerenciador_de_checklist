from tkinter import *

def adiciona_produto(estoque_adicionar, nome_adicionar, quantidade_adicionar):

    if nome_adicionar in estoque_adicionar:
        estoque_adicionar[nome_adicionar] += quantidade_adicionar

    else:
        estoque_adicionar[nome_adicionar] = quantidade_adicionar


def remover_estoque(estoque_remover, nome_remover, quantidade_remover):
    if nome_remover in estoque_remover:
        quantidade_em_estoque = estoque_remover[nome_remover]

        if quantidade_remover < quantidade_em_estoque:
            estoque_remover[nome_remover] -= quantidade_remover
            print(f'{quantidade_remover} de {nome_remover} removido do estoque.')

        elif quantidade_remover == quantidade_em_estoque:
            estoque_remover.pop(nome_remover)
            print(f'{nome_remover} removido completamente do estoque.')

        else:
            print(f'A quantidade informada é maior do que o estoque. Estoque: {estoque_remover[nome_remover]}')

    else:
        print(f'O produto {nome_remover} não se encontra no estoque')


def mostrar_estoque(estoque):
    print(f'O estoque atual é: \n')
    for nome_estoque, quantidade_estoque in estoque.items():
        print(f'{nome_estoque}: {quantidade_estoque}')



estoque = { 'Maçã' : 50, 'Laranja' : 32, 'Morango' : 47}


while True:

    mostrar_estoque(estoque)
    acao = input('\nEscolha uma ação: Adicionar, Remover, Mostrar estoque, Sair \n')


    match acao:
        case 'Adicionar' |  'adicionar':
            produto_a_adicionar = input('Informe o nome do produto a adicionar: \n')
            produto_a_adicionar = produto_a_adicionar.title()
            quantidade_a_adicionar = ''

            try:
                quantidade_a_adicionar = int(input('Informe a quantidade de produtos: \n'))
                confirmar_adicao = input(f'Confirmar a operação: Adicionar {produto_a_adicionar} | Quantidade:'
                                         f'{quantidade_a_adicionar} (Confirmar | Cancelar) \n')
                if confirmar_adicao == 'Confirmar':
                    adiciona_produto(estoque, produto_a_adicionar, quantidade_a_adicionar)
                else:
                    pass

            except ValueError:
                print(f'Digite apenas números inteiros.')

        case 'Remover' | 'remover':
            produto_a_remover = input('Informa o produto a remover: \n')
            produto_a_remover = produto_a_remover.title()
            quantidade_a_remover = ''

            try:
                quantidade_a_remover = int(input('Informe a quantidade de produtos a remover: \n'))
                confirmar_remocao = input(f'Confirmar a operação: Remover {produto_a_remover} | Quantidade:'
                                          f'{quantidade_a_remover} (Confirmar | Cancelar) \n')

                if confirmar_remocao == 'Confirmar':
                    remover_estoque(estoque, produto_a_remover, quantidade_a_remover)
                else:
                    pass

            except ValueError:
                print(f'Digite apenas números inteiros.')


        case 'Mostrar estoque' | 'mostrar estoque':
            mostrar_estoque(estoque)

        case 'Sair' | 'sair':
            break

        case _:
            print(f'Opção {acao} inválida. \n')


