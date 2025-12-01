# Enumerate vai gerar pares indice e valor  (indice, valor)
"""
cores = ['verde', 'vermelho', 'amarelo', 'azul']
indice = 0

for indice, cor in enumerate(cores):
    print(indice, cor)
    indice += 1

# encontrar o índice de um elemento em uma lista
filmes = ['pulp fiction', 'jango livre' , 'era uma vez em hollywood', 'tenet', 'inception']

print(filmes.index('jango livre'))

# começa a buscar a partir do índice 3
print(filmes.index('jango livre', 3))

# começa a buscar a partir do índice 3 e varre até o índice 4
print(filmes.index('jango livre', 3, 4))

"""

# é possível varrer listas com slice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[1:])

# começa em 1 e vai até o final de 2 em 2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[1::2])

# inverte a posição da lista ao imprimir
nome = 'Guilherme Wagner Domanski'
print(nome[::-1])

    