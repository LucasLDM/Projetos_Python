from Despesa import Despesa

class CalculadoraDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, descricao, valor, data):
        despesa = Despesa(descricao, valor, data)
        self.despesas.append(despesa)

    def remover_despesa(self, descricao):
        for desp in self.despesas:
            if desp.descricao == descricao:
                self.despesas.remove(desp)
                break

    def calcular_total_despesas(self):
        total = 0
        for desp in self.despesas:
            total += desp.valor
        print(f'Total gasto: {total}')
    
    def listar_despesas(self):
        for desp in self.despesas:
            print(f'Descrição: {desp.descricao}')
            print(f'Valor: {desp.valor}')
            print(f'Data: {desp.data}')
            print('----------------------')

    def maior_despesa(self):
        if not self.despesas:
            print('Não há despesas registradas.')

        maior_despesa = max(self.despesas, key=lambda despesa: despesa.valor)
        print(f'Maior despesa: {maior_despesa.valor}')
            
calculadora = CalculadoraDespesas()

calculadora.adicionar_despesa('Compras', 1300, '27-05-2023')
calculadora.adicionar_despesa('Restaurante', 520, '23-05-2023')
calculadora.adicionar_despesa('Academia', 159, '21-04-2023')
calculadora.listar_despesas()
calculadora.calcular_total_despesas()
calculadora.maior_despesa()
