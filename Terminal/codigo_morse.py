# Projeto para converter uma frase em código Morse.

def transformador_morse(texto:str):
    
    codigo = []

    for letra in texto:
        if letra in alfabeto:
            morse = alfabeto[letra]
            codigo.append(morse)
    return codigo
        
alfabeto = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..'
}

frase = input('Escreva algo: ').upper()
codigo_morse = ''.join(transformador_morse(frase))

print('A sua frase em código morse é: ', codigo_morse)
