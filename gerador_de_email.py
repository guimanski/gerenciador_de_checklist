def formatar_email(nome, dominio):

    nome_formatado = nome.lower().title()

    email_formatado = nome.lower().replace(' ', '_')

    if dominio.startswith('@'):
        dominio = dominio.replace('@', '')

    return nome_formatado, f"{email_formatado}@{dominio}"

nome = input('Informe seu nome completo: ')
dominio = input('Informe seu dominio (Ex: gmail.com | yahoo.com.br | @gov.br): ')


nome_formatado, email_formatado = formatar_email(nome, dominio)

print(f"Bem-vindo(a) {nome_formatado}. Seu e-mail é: {email_formatado}.")

# pra cara número de 1 até 20, imprima número num passo de 2 em 2
for numero in range (1, 20, 2):
    print(numero)
