from random import choice, randint

MIN_LENGTH = 4
MAX_LENGTH = 9

vocales = ('a', 'e', 'i', 'o', 'u', 'y')
consonantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
                 'sh', 'zh', 'ch', 'kh', 'th')

def nick():
    vocales = globals()['vocales']
    consonantes = globals()['consonantes']

    vocales_primero = bool(randint(0, 1))
    resultado = ''
    for i in range(0, randint(MIN_LENGTH, MAX_LENGTH)):
        es_par = i % 2 == 0
        if (vocales_primero and es_par) or (not vocales_primero and not es_par):
            resultado+=choice(vocales)
        else:
            resultado+=choice(consonantes)

    return resultado.title()
