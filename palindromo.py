# O código verifica se o texto fornecido pelo usuário é um palíndromo
# Palindromo é toda palavra ou frase que pode ser lida de trás pra frente e que, independente da direção, mantém o seu sentido.

def verifica_palindromo(texto):
    texto = texto.replace(' ', '').lower()

    if texto == texto[::-1]:
        return True
    else:
        return False

texto_usuario = input('Digite algo: ')

if(verifica_palindromo(texto_usuario)):
    print('É um palindromo')
else:
    print('Não é palindromo')