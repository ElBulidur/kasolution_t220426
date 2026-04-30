
class Aluno:
    def __init__(self, v_nome):
        self.nome = v_nome
        self.cursos_cadastrado = []
        
    def get_aluno(self):
        return f"Nome do aluno: {self.nome}, cursos cadastrados: {len(self.cursos_cadastrado)}"
        
    def __repr__(self):
        return self.nome
        