# ORIENTADA A OBJETO
# CLASSE


# ABSTRAÇÃO
# OBJETO
# PROPRIEDADE OU ATRIBUTO
# METODOS

class Carro:
    def __init__(self, v_cor, marca):
        self.cor = v_cor
        self.marca = marca
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, v_cor):
        self.__cor = v_cor
        
    def buzinar(self):
        print("Bi bi!")
    
    

fusca = Carro("Vermelho", "Volkswagem")

print(f"Classe: {Carro}")
print(f"Objeto: {fusca}")
print(f"Propriedade: {fusca.cor}")
print(f"Atributo: {fusca.marca}")
fusca.buzinar()