class Soma:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        
        self.resultado = self.__somar()
        
    def __somar(self):
        return self.numero_1 + self.numero_2