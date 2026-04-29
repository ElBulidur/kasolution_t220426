
class Aluno:
    def __init__(self, nome, turma, curso="Programando com Python"):
        self.nome = nome
        self.turma = turma
        self.curso = curso
        
    def cadastrar_no_banco(self):
        print("Cadastro realizado com sucesso!")
        
    def atualizar_dados(self, turma=None, curso=None):
        if turma:
            self.turma = turma
        if curso:
            self.curso = curso
        
julio = Aluno("Julio Pereira", "Turma da Alegria", "Palhaçaria")

julio.cadastrar_no_banco()
julio.atualizar_dados("Turma mudada")
    
print(julio.nome)
print(julio.turma)
print(julio.curso)