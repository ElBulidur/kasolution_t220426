# COMANDOS DE DECISÕES

usuario = "julio"
senha = "123"

# if usuario == "julio" and senha == "1243":
#     print("Logado com sucesso!!!")
# else:
#     print("Erro de usuario ou senha!")

nota = 7.0

# Se o aluno tiver abaixo de 7, REPROVADO
# Se tiver maior ou igual a 7, APROVADO

# if nota > 7.0:
#     print("APROVADO")

# if nota < 7:
#     print("REPROVADO!!!")


# if nota < 7.0:
#     print("REPROVADO")
# else:
#     print("APROVADO")


# Se o aluno tiver abaixo de 6, REPROVADO
# Se o aluno tiver 6 entre 6.9, RECUPERAÇÃO
# Se tiver maior ou igual a 7, APROVADO

nota = 6

# if nota < 6: print("REPROVADO")
# elif nota >= 6 and nota < 7: print("RECUPERAÇÃO")
# else: print("APROVADO")


# print("REPROVADO") if nota < 6 else print("APROVADO")

# nota =6

# if nota < 6:
#     print("reprovado")
# elif nota > 6 and nota < 7: print("RECUPERAÇÃO")
# #
# elif nota == 6:
#     pass
# else: print("APROVADO")

# COLEÇÕES
# MUTAVEIS
# LISTA
lista = ["Julio", 19, 1.72, True, 19]

# print(lista[0])
# print(lista[-1])
# print( type(lista) )
# print( dir(lista) )

lista[2] = 2.90

# res = lista.clear() # Limpa a lista e não retorna
# res = lista.append(20) # adcionar um objeto no final da lista e não retorna
# res = lista.count(19) # retorna o numero de ocorrencias.7
# res = lista.pop() # retorna o ultimo objeto da lista e remova ele.

# res = lista.remove(19) # remove a primeira ocorrencia do valor.


lista = [1, 6, 0, 3]
lista = ["Julio", "Ana", "Leonardo", "Ricardo"]

# res = lista.insert(1, "Alex")

# res = lista.sort(reverse=True)


# print(res)
# print(lista)

# print(  len(lista) ) # tamanho da lista

# DICIONÁRIOS

aluno = {"Aluno": "Julio", "Turma": 10, "Altura": 1.72, "Aprovado": True}

# print( type(aluno) )
# print(aluno.get("Alunos")) # procura a chave digitada

# print(aluno["Alunos"]) # precisa ser a mesma chave

# res = aluno.values()

res = list(aluno.keys())

res = aluno.items()


# print(res)

# print(aluno)

# IMUTAVEIS

# TUPLA

lista = [2, 5, 7]
tupla = (2, 5, 7)


# lista[0] = 25
# tupla[0] = 25

# tupla.insert(0, 25)

# print(dir(tupla))

# print(res)
# print(lista)
# print(tupla)


# LOOPS DE REPETIÇÕES
lista = ["Julio", "Ana", "Leonardo", "Ricardo"]
# print(range(10))

# for x in range(5):
#     print(x)

# for x in lista:
#     print(x)

# for x in range( len(lista) ):
#     print(x)


lista = [1, 3, 6, 0, 3, 3]

# lista.remove(3)
remover = 3

for x in range(lista.count(remover)):
    lista.remove(remover)
    if x == 1:
        break


# for x in range(5):
#     print(x)

# [print(x) for x in range(5)]

meus_numeros = [i for i in lista if i in (0, 6)]

# print(meus_numeros)

aluno = {
    "Aluno": "Julio",
    "Turma": 10,
    "Altura": 1.72,
    "Aprovado": True,
    "notas": [6, 8, 7, 5],
}


bimestres = [
    [f"Bimestre 0{valores+1}: {valor[valores]}" for valores in range(len(valor))]
    for chave, valor in aluno.items()
    if chave == "notas"
]

# print(bimestres)

# for chave, valor in aluno.items(): print(x)

numeros = [1, 5, 9, 8, 7]

num = 5

for x in numeros:
    if x == num:
        print("Parabens!!!")
        break
else:
    print("Sem sorte!")
