def encontrar_palindromo(palavra):
    palavra = palavra.lower()
    list_palavra = list(palavra)
    list_palavra_inverso = list_palavra[::-1]

    print(list_palavra)
    print(list_palavra_inverso)

    letras_para_remover = []

    i = 0
    j = 0

    for artel in list_palavra:
        for letra in list_palavra_inverso:
            if list_palavra_inverso[i] == list_palavra_inverso[j]:
                continue
            else:
                letras_para_remover.append(letra)
            i = i + 1
        i = 0
        j = j + 1

    for letra in letras_para_remover:
        list_palavra.remove(letra)
        letras_para_remover.remove(letra)


    palavra_final = ''.join(list_palavra)
    print(palavra_final)

palavra = input('Digite uma palavra: ')
encontrar_palindromo(palavra)
