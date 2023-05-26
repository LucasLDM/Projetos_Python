# Um programa que gera senhas aleatórias com base em requisitos definidos pelo usuário, como comprimento da senha e os tipos de caracteres a serem utilizados (letras maiúsculas, letras minúsculas, números e caracteres especiais.

import random

def gerar_senha(lista: list):
    senha_gerada = []
    for _ in range(comprimento_senha):
        elemento_aleatorio = random.choice(lista)
        senha_gerada.append(elemento_aleatorio)
    return senha_gerada

comprimento_senha = int(input('Comprimento da senha: '))

letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
caracteres_especiais = '!@#$%¨&*()-+[]'

tipos_caracteres = int(input('''

    1. Maiúsculas
    2. Minúsculas
    3. Caracteres especiais

    Qual o tipo de caractere desejado?
    -> '''))

match tipos_caracteres:
    case 1:
        senha = gerar_senha(letras_maiusculas)
    case 2: 
        senha = gerar_senha(letras_minusculas)
    case 3: senha = gerar_senha(caracteres_especiais)

print('Senha gerada: ', ''.join(senha))
