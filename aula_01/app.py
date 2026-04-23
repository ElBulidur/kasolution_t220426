# VARIÁVEIS
# Snake_case = julio_pereira, julio_pereira_silva


nome = "julio" # string(str)
idade = 12 # inteiro(int)
altura = 12.5 # Real(float)
aprovado = True # Boleana(bool)

resposta = 10 > 5 < 45 > 85 > 95

aula_01 = "Correr"


# print("Nome = ", nome,", Tipo => ", type(nome))
# print("Var resposta = ", resposta,", Tipo => ", type(resposta))

# print( nome  )
# print( nome.capitalize()  )
# print( nome.upper()  )

# print( dir(nome) )


# atribuir valores

numero = 123
numero_01, numero_02 = 10, 20
numero_03 = numero_04 = 10

# print(numero_01, numero_02, numero_03, numero_04)


numeros_1_10 = (x for x in range(1, 10))

# print(numeros_1_10)
# print(type(numeros_1_10))

# print("===== PEGANDO O NOME ======")
# nome = input("Digite o seu nome: ")

# print("Seja bem vindo, ", nome)

# OPERADORES (+ - / *)

# try:
#     n_01 = int( input("Digite o primeiro numero: ") )
#     n_02 = int(input("Digite o segundo numero: "))
# except:
#     raise ValueError("Só aceita numero! tente de novo.")

# castear

# print(n_01 + n_02)

# OPERADORES MATEMÁTICOS (+ - / *)

n1 = 10
n2 = 42
n3 = 12
n4 = 13

res = n1 + n2
res = n1 - n2
res = n1 * n4
res = n1 / n4


res = n1 / n4 # Divisão Real 10 / 13 = 
res = n1 // n4 # Divisão inteira 10 // 13 = 0
res = n1 % n4 # Resto da divisão 

n1 = n1 + 10
n1 += 10

# print(n1)

# OPERADORES RELACIONAIS ( > < == !=)
# print(n1 == n2)
# print(n1 != n2)
# print(n1 > n2)
# print(n1 < n2)
# print(n1 >= n2)
# print(n1 <= n2)

# OPERADORES LÓGICO ( or and not)
# print(True or False)
# print(True and False)
# print(not True and False)

print(n1 == n2 or n1 > n2)