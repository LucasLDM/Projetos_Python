# Fazer um TODO list o qual  permitirá que o usuário adicione tarefas, marque tarefas como concluídas, liste as tarefas pendentes e remova tarefas da lista

class Tarefa:
    def __init__(self, descricao, concluida, data):
        self.descricao = descricao
        self.concluida = concluida
        self.data = data