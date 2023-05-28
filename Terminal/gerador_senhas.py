# Gerador de senhas seguras
import random

letra_maiuscula = chr(random.randint(65, 91))
letra_minuscula = chr(random.randint(97, 123))
char_especial = chr(33)
lista_numeros = []

for i in range(5): # até 8 dígitos
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros)[1:-1].replace(',','') # remove as chaves e vírgulas
print(letra_maiuscula, letra_minuscula, lista_numeros, char_especial)











