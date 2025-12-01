"""
Dicionários:

OBS: Em algumas linguagens de programação os dicionários python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.


Dicionários são representados por {}

OBS: Chave e valor são separados por dois pontos 'Chave': 'Valor"
    Tanto chave quanto valor podem ser de qualquer tipo de dado
    Podemos misturar tipos de dados

# Criação de dicionários:

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país')
else:
    print('Não encontrei o país')
# Em pyhton o tipo None sempre vai ser falso

# Podemos ter um valor padrão para ser impresso caso a chave não seja encontrada
pais = paises.get('ru', 'Não Encontrado')
print(pais)

# Acessando Elementos:

# Forma 1 - Acessando via chave, da mesma forma que na lista/tupla
print(paises['br'])
print(paises['py'])
# OBS: Se a chave que tentamos acessar não existir, teremos o erro KeyError

#Forma 2 - Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('ru'))
#OBS: Dessa forma, se a chave não existir retorna None, não retorna erro

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
print(paises)


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuplas dicionários,
# como chaves de dicionários

# Tuplas são bastante interessantes de serem usadas como chaves de dicionários, pois são imutáveis
localidades = {
    (45.123, 51.1234): 'Escritório em Tókio',
    (42.125, 98,1235): 'Escritório em Nova York',
    (42.113, 65,1235): 'Escritório em São Paulo',

}

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar':300}

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos dados e de atualizar dados já existentes é a mesma;
# CONCLUSÃO 2: Em dicionários, não podemos ter chaves repetidas.

# Remover dados de um dicionário:

receita = {'jan': 100, 'fev': 120, 'mar':300}
print(receita)

# Forma 1 - Mais comum
receita.pop('mar')
print(receita)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado

# Forma 2
del receita['fev']
print(receita)
# Se a chave não existir será gerado um KeyError
# OBS: Nesse caso o valor removido não é retornado

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

# Limpar o dicionário
d.clear()

# Copiar um dicionário para outro

# Forma 1 - Deep Copy
novo = d.copy()
novo['d'] = 4

# Forma 2 - Shallow Copy
novo = d
novo['d'] = 4

"""
# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

# O metodo fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a essa chave o valor informado