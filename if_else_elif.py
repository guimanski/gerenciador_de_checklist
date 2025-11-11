"""
Estruturas condicionais
if, else, elif
"""
import datetime


def maioridade(ano_nascimento):

    ano_atual = datetime.date.today().year
    global pode_acessar

    if ano_atual - ano_nascimento < 18:
        pode_acessar = False
    if ano_atual - ano_nascimento >= 18:
        pode_acessar = True


def formatar_nome(nome):
    return nome.title()


nome = input('Digite seu nome: ')
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
pode_acessar = False

maioridade(ano_nascimento)


if not pode_acessar:
    print(f'Olá, {formatar_nome(nome)}! Seja bem-vindo(a)! Por ter menos de 18 anos, seu acesso foi negado!')

elif pode_acessar:
    print(f'Olá, {formatar_nome(nome)}! Seja bem-vindo(a)! Por ter mais de 18 anos, seu acesso foi aprovado!')

for valor in enumerate(nome):
    print(valor)
