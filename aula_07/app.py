
from mimesis import Person
from mimesis.locales import Locale

from persistencia import DBPersistencia

from datetime import date
from random import randint as rdi


db_simples = DBPersistencia("sql")

# CREATE
# db_simples.create([date.today(), "Rafael", 99], "alunos")

# READ
# print( db_simples.read("alunos", 3803) )

# UPDATE
# db_simples.update("alunos", 150, 3803)

# DELETE
# db_simples.delete("alunos", 3803)


db_alchemy = DBPersistencia("sqlalchemy")


# try:
#     conn = db_alchemy.get_conection()
#     print(conn)
# except Exception as e:
#     print(e)

# db_alchemy.create([date.today(), "Julio", 99], "alunos")

# READ
# print( db_alchemy.read("alunos", 3804) )


db_alchemy.update("alunos", 150, 3809)
