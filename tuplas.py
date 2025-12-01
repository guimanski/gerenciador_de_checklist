"""
Tuplas

Tuplas são bastante parecidas com listas. Existem duas diferenças básicas:

As tuplas são representadas por () enquanto listas são representadas por []

As tuplas são imutáveis. Toda operação em uma tupla, gera uma nova tupla

# Cuidado 1: As tuplas são representadas por (), mas se houver somente um elemento, pode não ser interpretado como
# uma tupla

#uma forma de gerar uma tupla sequencial é utilizando range (lembrando que o range [inicio, fim, passo] não inclui o
# último elemento)

tuple = tuple(range(11))
print(tuple)

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato de tuplas serem imutáveis

# é possível concatenar tuplas, mas seus valores não se alteram

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

tupla1 = tupla1 + tupla2 #tuplas são imutáveis mas é possível sobreescrever os seus valores

print(3 in tupla1) # retorna valor booleano

# Contando elementos em uma tupla

tupla = ('a', 'b', 'c')
print(tupla.count('a'))

"""



