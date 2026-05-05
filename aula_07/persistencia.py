from mimesis import Person, Address
from mimesis.locales import Locale
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from config_db import ConfigDB
import mysql.connector

from aluno import Aluno

class Persistencia:
    def __init__(self, tipo):
        self.tipo = tipo
     
    def get_conection(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclase") 
        
    def create(self, data, destino=None):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def read(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def update(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def delete(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
class ArquivoPersistencia(Persistencia):
    def __init__(self, tipo):
        super().__init__(tipo)
        
    def create(self
               , nome_arquivo:str, data:list = []
               , cabecalho=None, fake=False
               , qtd=10, extensao="txt"
            ):
        if fake:
            print("1 - Pessoa, 2 - Endereço")
            
            opcao = input("Qual mock vc quer(Escolha um numero): ")
            
            
            mock = None
            if opcao == "1":
                cabecalho="Nome_Completo"
                mock = Person(Locale.PT_BR)
                
                for _ in range(1, qtd+1):
                    data.append(mock.full_name())
            
            elif opcao == "2":
                cabecalho="Endereço_Completo"
                mock = Address(Locale.PT_BR)
                
                for _ in range(1, qtd+1):
                    data.append(mock.address())
            else:
                print("Ops! errou!")
                
            
        with open(nome_arquivo, "w") as arq:
            if cabecalho:
                arq.write(cabecalho+"\n")
            
            for item in data:
                arq.write(item+"\n")
                
    def read(self, arquivo):
        
        with open(arquivo, "r") as arq:
            res = arq.readlines()
            
        return res
    
    def update(self, arquivo, antigo_dado, novo_dado):
        
        partes = arquivo.split(".")
        
        arquivo_atualizado = f"{partes[0]}_atualizado.{partes[1]}"
        
        with open(arquivo, "r") as arq:
                res = arq.readlines()
        
        novo_data = []
        
        for linha in res:
            if linha != antigo_dado:
                novo_data.append(linha)
            else:
                novo_data.append(novo_dado)
                
        with open(arquivo_atualizado, "w") as arq:
            
            for item in novo_data:
                arq.write(item)
                
        print("Arquivo criado com atualização.")
                          
    def delete(self, arquivo, dado_deletar):
        
        with open(arquivo, "r") as arq:
                res = arq.readlines()
        
        novo_data = []
        
        for linha in res:
            if linha != dado_deletar:
                novo_data.append(linha)
                
        with open(arquivo, "w") as arq:
            
            for item in novo_data:
                arq.write(item)
                
        print("Dado deletado do arquivo com sucesso.")
            
class DBPersistencia(Persistencia):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.config = ConfigDB()
        
        self.session = None
        
    def get_conection(self):
        if self.tipo == "sql":
            try:
                conn = mysql.connector.connect(**self.config.pegar_config_db())
                
                return conn
            except Exception as e:
                print(e)
        if self.tipo == "sqlalchemy":
            self.engine = create_engine(self.config.pegar_url_db())
            
            self.session = Session(self.engine)
            
                
    def create(self, dados, tabela):
        
        if self.tipo == "sql":
            sql = f"INSERT INTO {tabela} (create_time, name, nota) values (%s, %s, %s)"
            
            conn = self.get_conection()
            
            cursor = conn.cursor()

            cursor.execute(sql, dados)

            conn.commit()
            conn.close()
            
            print(f"Aluno {dados[1]} criado com sucesso!")
            
        if self.tipo == "sqlalchemy":
            self.get_conection()
            
            if tabela == "alunos":
                novo_aluno = Aluno(
                    create_time=dados[0],
                    name=dados[1],
                    nota=dados[2]
                )
                
                self.session.add(novo_aluno)
                
                self.session.commit()
            
          
    def read(self, tabela, id:int=None):
        
        if self.tipo == "sql":
            if not id:
                sql = f"select * from {tabela}"

                conn = self.get_conection()

                cursor = conn.cursor()

                cursor.execute(sql)
                
                return cursor.fetchall()
            else:
                sql = f"select * from {tabela} where id=%s"

                conn = self.get_conection()

                cursor = conn.cursor()

                cursor.execute(sql, [id])

                return cursor.fetchone()
            
        if self.tipo == "sqlalchemy":
            # self.get_conection()
            
            if tabela == "alunos":
                
                if id:
                    stmt = select(Aluno).where(Aluno.id == id)
                else:
                    stmt = select(Aluno)
                
                alunos = []
                
                if not self.session:
                    self.get_conection()
                
                for aluno in self.session.scalars(stmt):
                    alunos.append(aluno)
                    
                return alunos

    def update(self, tabela, nova_nota, id):
        
        if self.tipo == "sql":
            sql = f"UPDATE {tabela} SET nota=%s where id=%s"
            conn = self.get_conection()

            cursor = conn.cursor()

            cursor.execute(sql, [nova_nota, id])

            if cursor.rowcount:
                conn.commit()
                conn.close()
                print(f"Aluno com id {id} atualizado com sucesso!")
            else:
                print(f"O aluno com {id} não foi encontrado no banco de dados!")
                conn.close()
                
        if self.tipo == "sqlalchemy":
            if not self.session:
                    self.get_conection()
                    
            stmt = select(Aluno).where(Aluno.id == id)
            try:
                aluno = self.session.scalars(stmt).one()
                
                aluno.nota = nova_nota
                
                self.session.commit()
                    
                print(f"Aluno com id {id} atualizado com sucesso!")
            
            except:
                print(f"O aluno com {id} não foi encontrado no banco de dados!")

    
    def delete(self, tabela, id):
        sql = f"DELETE from {tabela} where id=%s"

        conn = self.get_conection()

        cursor = conn.cursor()

        cursor.execute(sql, [id])

        if cursor.rowcount:
            conn.commit()
            conn.close()
            print(f"Aluno do id {id} foi deletado com sucesso!")
        else:
            print(f"Aluno com id {id} não foi encontrado no banco de dados ou já foi deletado!")
            conn.close()