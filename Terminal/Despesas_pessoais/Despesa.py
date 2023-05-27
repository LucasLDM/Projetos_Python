# Crie um programa que permita aos usuários registrar suas despesas pessoais e realizar cálculos com base nessas despesas.

class Despesa:
    def __init__(self, descricao, valor, data):
        self.descricao = descricao
        self.valor = valor
        self.data = data
