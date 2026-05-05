import mysql.connector
from mimesis import Person
from mimesis.locales import Locale

from datetime import date
from random import randint as rdi


def pergar_conexao():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="kasolution",
            port = "3306"
        )
        
        # print("Conectado com sucesso!!!")
        return conn
    except Exception as e:
        print(e)
        

# create_time => Data
# Name => string
# Nota => int

#  CREATE
def criar_aluno(dados: list):
    try:
        sql = "INSERT INTO alunos (create_time, name, nota) values (%s, %s, %s)"

        conn = pergar_conexao()
        cursor = conn.cursor()

        cursor.execute(sql, dados)

        conn.commit()
        conn.close()
    except:
        conn.rollback()
        conn.close()

    print(f"Aluno {dados[1]} salvo no banco de dados com sucesso!")


# criar_aluno([date.today(), "Rafael", 99])

# READ

def pegar_alunos():
    sql = "select * from alunos"

    conn = pergar_conexao()

    cursor = conn.cursor()

    cursor.execute(sql)
    
    return cursor.fetchall()

    # print( [linha for linha in cursor ] )
    # print(cursor.fetchone())
    # print( cursor.fetchall())
    # print(cursor.fetchmany(2))
    
# alunos = pegar_alunos()
# print(alunos)

def pegar_aluno_pelo_id(id):
    sql = "select * from alunos where id=%s"

    conn = pergar_conexao()

    cursor = conn.cursor()

    cursor.execute(sql, [id])

    return cursor.fetchone()

# aluno_3 = pegar_aluno_pelo_id(3)
# print(aluno_3)

# UPDATE
def atualizar_nota_pelo_id(nova_nota, id):
    sql = "UPDATE alunos SET nota=%s where id=%s"
    conn = pergar_conexao()

    cursor = conn.cursor()

    cursor.execute(sql, [nova_nota, id])

    if cursor.rowcount:
        conn.commit()
        conn.close()
        print(f"Aluno com id {id} atualizado com sucesso!")
    else:
        print(f"O aluno com {id} não foi encontrado no banco de dados!")
        conn.close()

# atualizar_nota_pelo_id(150, 3)

# DELETE
def deletar_aluno_pelo_id(id):
    sql = " DELETE from alunos where id=%s"

    conn = pergar_conexao()

    cursor = conn.cursor()

    cursor.execute(sql, [id])

    if cursor.rowcount:
        conn.commit()
        conn.close()
        print(f"Aluno do id {id} foi deletado com sucesso!")
    else:
        print(f"Aluno com id {id} não foi encontrado no banco de dados ou já foi deletado!")
        conn.close()


# deletar_aluno_pelo_id(1)

def limpar_banco():
    alunos = pegar_alunos()
    
    for aluno in alunos:
        deletar_aluno_pelo_id(aluno[0])
    
    
# limpar_banco()


def popular_banco(qtd):
    
    for _ in range(qtd):
        aluno = Person(Locale.PT_BR).full_name()
        nota = rdi(5,11)
        criar_aluno([date.today(), aluno, nota])
    

# popular_banco(5000)

# print( f"Quantidade de alunos no banco: {len(pegar_alunos())}" )

