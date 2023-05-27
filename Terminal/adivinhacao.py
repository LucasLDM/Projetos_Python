from random import randint

def esta_proximo():
    if palpite > numero:
        print('Está frio')
    else:
        print('Está quente')

numero = randint(1, 11)
tentativas = 0

palpite = int(input('Estou pensando em um número de 1 a 10\nQual será ele? -> '))

while palpite != numero:

    try:
        while palpite != numero:
            tentativas += 1
            esta_proximo()
            palpite = int(input('Tente novamente. Palpite: '))
            if palpite == numero:
                break
    except ValueError:
        print('O valor é um número, tente novamente!')

print(f'O número era {numero}! Bom jogo!')
print(f'Tentativas: {tentativas+1}')