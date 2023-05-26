# Crie um programa que permita ao usuário calcular seu Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.

def checar_imc(imc):
    if imc < 18.5:
        print(f'Abaixo do peso. IMC: {imc} (Magreza excessiva)')
    elif 18.5 < imc < 24.9:
        print(f'Peso normal. IMC: {imc} (Saudável)')
    elif 25 < imc < 29.9:
        print(f'Sobrepeso. IMC: {imc} (Acima do peso recomendado)')
    elif 30 < imc < 34.9:
        print(f'Obesidade grau 1. IMC: {imc} (Moderada)')
    elif 35 < imc < 39.9:
        print(f'Obesidade grau 2. IMC: {imc} (Severa)')
    else:
        print(f'Obesidade mórbida. IMC: {imc} (Muito severa)')

try:
    peso = float(input('Seu peso em quilogramas (kg): '))
    altura = float(input('Sua altura em metros (m): '))
    imc = peso / (altura * altura)
    imc = round(imc, 2)
    checar_imc(imc)

except ValueError:
    print('Escolha valores válidos! Apenas números são permitidos.')
