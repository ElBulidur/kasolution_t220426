from mod import *

class Main:
    def __init__(self):
        print("="*50)
        print("======== CALCULADORA =============")
        print("="*50)
        print("")
        
        self.numero_1 = input("Digite o PRIMEIRO numero: ")
        self.numero_2 = input("Digite o SEGUNDO numero: ")
        self.opt = input("Escolha a operação (+, -, /, *): ")
        
        self.__validar_dados()
        
        if not self.__verificar_opt():
            print("A calculadora só aceita as operações +, -, /, *.")
            print("Calculadora finalizada!")
            
        self.__realizar_calculo()
        
    def __verificar_opt(self):
        if self.opt in ("+", "-", "/", "*"):
            return True
        else:
            return False
        
    def __validar_dados(self):
        try:
            self.numero_1, self.numero_2 = int(self.numero_1), int(self.numero_2)
        except:
            try:
                self.numero_1, self.numero_2 = float(self.numero_1), float(self.numero_2)
            except:
                print("Infelizmente você colocou valores errados!!!")
                print("Calculadora finalizada!")
        
    def __realizar_calculo(self):
        if self.opt == "+":
            resposta = Soma(self.numero_1, self.numero_2).resultado
            
            print(f"O resultado da soma de {self.numero_1} + {self.numero_2} é: {resposta}")
        elif self.opt == "-":
            resposta = Sub(self.numero_1, self.numero_2).resultado
            
            print(f"O resultado da subtração de {self.numero_1} - {self.numero_2} é: {resposta}")
        elif self.opt == "/":
            resposta = Divisao(self.numero_1, self.numero_2).resultado
            
            print(f"O resultado da divisão de {self.numero_1} / {self.numero_2} é: {resposta}")
        elif self.opt == "*":
            resposta = Mult(self.numero_1, self.numero_2).resultado
            
            print(f"O resultado da multiplicação de {self.numero_1} * {self.numero_2} é: {resposta}")



if __name__ == "__main__":
    Main()