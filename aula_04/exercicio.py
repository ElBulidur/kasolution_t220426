"""
    Laboratório 01

    Este programa representa um jogo para adivinhar números. Os passos são apresentados a seguir, com um 
    exemplo de uso:

        => O programa produz um número aleatório inteiro entre 1 e 100 (suponha: 49);
        => O programa pede para o usuário: "Informe um valor entre 0 e 100": 60;
        => Como o número informado é maior que o produzido, o programe pede: "Informe um valor entre 0 e 59" : 20;
        => Como o número informado é menor que o produzido, o programa pede: "Informe um valor entre 21 e 59";
        => No final, o programa apresenta o número de tentativas.

    Observação: se o usuário fornece um valor fora da faixa solicitada, conta como tentativa.

"""
#  DICA
# USAR MODULO
from random import randint as rdi
import os

minimo, maximo = 1, 100
numero = rdi(minimo, maximo)
tentativas = 0

while True:
    tentativas += 1
    numero_usuario = int(input(f"Informe um nomero entre {minimo} e {maximo}: "))
    os.system("clear")
    
    if numero_usuario < minimo or numero_usuario > maximo: continue
    
    if numero_usuario < numero: minimo = numero_usuario + 1
    elif numero_usuario > numero: maximo = numero_usuario - 1
    else: break
    
print(f"Parabens! o numero sorteado foi  o {numero}")
print(f"Você acertou em {tentativas} tentativas.")
        






