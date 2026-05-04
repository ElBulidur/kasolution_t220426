from persistencia import ArquivoPersistencia


# CRUD ARQUIVO

arquivo = ArquivoPersistencia("arquivo")  
# arquivo.create("empresas.txt", fake=True, qtd=200000)

# retorno = arquivo.read("empresas.txt")
# [print(x[0:-2c]) for x in retorno]

# arquivo.update("empresas.txt"
#     , "Pedágio Praça Manoel Campos da Paz 454\n"
#     , "Pedágio Praça Manoel Campos da Paz 454 (ATUALIZADO)\n"
#     )

# arquivo.delete("empresas.txt"
#     , "Pedágio Praça Manoel Campos da Paz 454\n"
# )

# CRUD DB

