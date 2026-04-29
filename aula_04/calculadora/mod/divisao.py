class Divisao:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        
        self.resultado = self.__divisao()
        
    def __divisao(self):
        return self.numero_1 / self.numero_2
    