from aluno_entity import Aluno
# técnicos (Periodos, Disciplinas)
# Profissionalizante (Valor)

class Curso:
    def __init__(self, v_nome, v_descricao, v_carga_horaria):
        self.nome = v_nome
        self.descricao = v_descricao
        self.carga_horaria = v_carga_horaria
        self.alunos_cadastrados = []
        
    def cadastrar_aluno(self, v_aluno:Aluno):
        self.alunos_cadastrados.append(v_aluno)
        v_aluno.cursos_cadastrado.append(self.nome)
                
class CursoTecnico(Curso):
    def __init__(self, nome, descricao, carga_horaria, periodos: int, disciplinas: list):
        super().__init__(nome, descricao, carga_horaria)
        self.periodos = periodos
        self.disciplinas = disciplinas
        
    def cadastrar_aluno(self, v_aluno:Aluno, v_escola):
        
        if v_escola == "publica":
            self.alunos_cadastrados.append(v_aluno)
            v_aluno.cursos_cadastrado.append(self.nome)
        else:
            print("Este curso só aceita aluno de escola pública")
            
class CursoProfissionalizante(Curso):
    def __init__(self, nome, descricao, carga_horaria, v_valor: float):
        super().__init__(nome, descricao, carga_horaria)
        self.valor = v_valor

# python = Curso("Python", "Programando com Python", 32)

python_tecnico = CursoTecnico("Python Tec", "Programando com Python", 32, 2, ["Analises de dados", "Python para Web"])
python_profissional = CursoProfissionalizante("Python Prof", "Programando com Python", 32, 2.50)


aluno_julio = Aluno("Júlio")

# print(python)
# print(python.nome)
# print(python.descricao)
# print(python.carga_horaria)
# print(python.cadastrar_aluno())

python_tecnico.cadastrar_aluno(aluno_julio, "privada")
python_profissional.cadastrar_aluno(aluno_julio)

print( python_tecnico.alunos_cadastrados)
print( python_profissional.alunos_cadastrados)

print(aluno_julio.cursos_cadastrado)

print( aluno_julio.get_aluno())
