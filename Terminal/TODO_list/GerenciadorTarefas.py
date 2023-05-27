from Tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, concluida = False, data = None):
        tarefa = Tarefa(descricao, concluida, data)
        self.tarefas.append(tarefa)

    def marcar_concluida(self, descricao):
        for trf in self.tarefas:
            if trf.descricao == descricao:
                trf.concluida = True
                break
    
    def listar_tarefas_pendentes(self):
        print('[-- Tarefas pendentes --]')
        for trf in self.tarefas:
            if not trf.concluida:
                print(trf.descricao)
        print('-------------------------')


    def listar_tarefas_concluidas(self):
        print('[-- Tarefas concluídas --]')
        for trf in self.tarefas:
            if trf.concluida:
                print(f'Descrição: {trf.descricao}')
                print(f'Data: {trf.data}')
                print('---------------')

    def remover_tarefa(self, descricao):
        for trf in self.tarefas:
            if trf.descricao == descricao:
                self.tarefas.remove(trf)
    
gerenciador = GerenciadorTarefas()
gerenciador.adicionar_tarefa('Estudar python', True, '27-05-2023')
gerenciador.adicionar_tarefa('Revisar código', False, '27-05-2023')
gerenciador.adicionar_tarefa('Estudar inglês no duolingo')
gerenciador.listar_tarefas_pendentes()
gerenciador.listar_tarefas_concluidas()
