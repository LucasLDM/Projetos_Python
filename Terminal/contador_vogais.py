# Um programa que solicita ao usuário uma palavra ou frase e conta o número de vogais presentes nela. Não serão aceitas vogais repetidas.

texto = input('Escreva uma palavra ou frase: ').lower()
qtd_vogais = 0
vogais = ['a','e','i','o','u']
vogais_encontradas = []

for letra in texto:
    if(letra in vogais and letra not in vogais_encontradas):
        qtd_vogais += 1
        vogais_encontradas.append(letra)
        
print(f'Quantidade de vogais encontradas: {qtd_vogais}')
print(f'Vogais: {vogais_encontradas}')
