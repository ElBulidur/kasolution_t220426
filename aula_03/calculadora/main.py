from mod import *

def run():
    print("="*50)
    print("======== CALCULADORA =============")
    print("="*50)
    print("")
    
    numero_1 = input("Digite o PRIMEIRO numero: ")
    numero_2 = input("Digite o SEGUNDO numero: ")
    opt = input("Escolha a operação (+, -, /, *): ")
    
    if not opt in ("+", "-", "/", "*"):
        print("A calculadora só aceita as operações +, -, /, *.")
        print("Calculadora finalizada!")
    else:
        try:
            numero_1, numero_2 = int(numero_1), int(numero_2)
        except:
            try:
                numero_1, numero_2 = float(numero_1), float(numero_2)
            except:
                print("Infelizmente você colocou valores errados!!!")
                print("Calculadora finalizada!")
                
        if opt == "+":
            resposta = somar(numero_1, numero_2)
            
            print(f"O resultado da soma de {numero_1} + {numero_2} é: {resposta}")
        elif opt == "-":
            resposta = sub(numero_1, numero_2)
            
            print(f"O resultado da subtração de {numero_1} - {numero_2} é: {resposta}")
        elif opt == "/":
            resposta = div(numero_1, numero_2)
            
            print(f"O resultado da divisão de {numero_1} / {numero_2} é: {resposta}")
        elif opt == "*":
            resposta = mult(numero_1, numero_2)
            
            print(f"O resultado da multiplicação de {numero_1} * {numero_2} é: {resposta}")

    input("DIGITE QUALQUER COISA PARA SAIR!!!")   
    
if __name__ == "__main__":
    run()