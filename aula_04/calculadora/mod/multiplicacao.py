class Mult:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        
        self.resultado = self.__mult()
        
    def __mult(self):
        return self.numero_1 * self.numero_2
    