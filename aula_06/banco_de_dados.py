import mysql.connector


try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="kasolution"
    )
    
    # print("Conectado com sucesso!!!")
    # print("")
    # print("Cadastrando aluno no banco")
    
    # sql = "INSERT INTO alunos (name, nota) values (%s, %s)"
    
    # cursor = conn.cursor()
    
    # cursor.execute(sql, ["Julio Pereira", 100])
    
    # conn.commit()
    
    # conn.close()
    
    # print("Alunos cadastrado!!!")
    
    sql = "select * from alunos"
    
    cursor = conn.cursor()
    
    cursor.execute(sql)
    
    # print( [linha for linha in cursor ] )
    print(cursor.fetchone())
    
except:
    print("Deu erro!!!")
    
    
    
