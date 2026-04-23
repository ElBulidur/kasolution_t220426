"""
    Laboratório 1 
    Escrever um programa em Python que solicite informações de três pessoas, como nome, idade, peso e altura. 
    Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. Usar a formatação 
    de interpolação. 

"""

print("*"*35)
print("Digite os dados das três pessoas")
print("*"*35)
print("")
print("PRIMEIRA PESSOA")
nome_1, idade_1, peso_1, altura_1 = input("Nome: "), int(input("Idade: ")), float(input("Peso: ")), float(input("Altura: "))

print("")
print("SEGUNDA PESSOA")
nome_2, idade_2, peso_2, altura_2 = input("Nome: "), int(input("Idade: ")), float(input("Peso: ")), float(input("Altura: "))

print("")
print("TERCEIRA PESSOA")
nome_3, idade_3, peso_3, altura_3 = input("Nome: "), int(input("Idade: ")), float(input("Peso: ")), float(input("Altura: "))

print("")
print("Dados capturados:")
print(f"Primeira pessoa =>  Nome: {nome_1}, Idade: {idade_1}, Peso: {peso_1} e Altura: {altura_1}")
print(f"Segunda pessoa =>  Nome: {nome_2}, Idade: {idade_2}, Peso: {peso_2} e Altura: {altura_2}")
print(f"Terceira pessoa =>  Nome: {nome_3}, Idade: {idade_3}, Peso: {peso_3} e Altura: {altura_3}")

