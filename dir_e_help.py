"""
Utilitários de python

-> Dir: Apresenta todos os atributos/funções/métodos disponíveis para determinado tipo de dado ou variável

-> Help: Apresenta a documentação/como utilizar os atributos/propriedades e e funções disponíveis para determiado tipo
de dado ou variável

"""

import datetime

# entrada de dados
nome = input("Digite seu nome: ")

ano_nascimento = input("Digite seu ano de nascimento: ")

# processamento
ano_atual = datetime.date.today().year


# saída

# int(ano_nascimento) => cast
# cast é a 'conversão' de um tipo de dado em outro
# todos os dados recebidos como input são do tipo string

print(f'Seja bem-vindo(a) {nome.title()}. Sua idade é {ano_atual - int(ano_nascimento)} anos.')