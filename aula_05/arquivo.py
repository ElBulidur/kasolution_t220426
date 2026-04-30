#  PERSISTENCIA
import os

# alunos = ["Julio", "Ricardo", "Ana", "Willian", "Felix"]


# PRIMEIRA FORMA
# arquivo = open("alunos.txt", "w")
# arquivo.write("aluno\n")

# for aluno in alunos:
#     arquivo.write(f"{aluno}\n")

# arquivo.close()


#  SEGUNDA FORMA
# with open("aluno.txt", "w") as arquivo:
#     arquivo.write("aluno\n")
    
#     for aluno in alunos:
#         arquivo.write(f"{aluno}\n")


#  LEITURA
# with open("aluno.txt", "r") as arq:
#     # res = arq.read()
#     # res = arq.read(7)
#     res = arq.readline()
#     res = arq.readlines()


file = "aluno.txt"
pasta = "../aula_04"


# print("Tem o arquivo") if os.path.exists(file) else print("Não tem")

# print("É uma pasta") if os.path.isdir(pasta) else print("Não é pasta")

# print( os.getcwd() ) # Mostra aonde esta no momento atual

# os.chdir('..') # navega pelo caminho.

# print(os.listdir()) # lista arquivos e diretorio

# print( os.getcwd() ) 

# os.mkdir("JULIO") # cria pasta

# os.rmdir("JULIO")

# os.system("clear")
# os.system("dir")

res = os.getpid()

print(res)


#  CSV
#  EXCEL