
class Pessoa:
    def __init__(self, nome, idade=None, peso=None, altura=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, v_nome):
        self.__nome = v_nome
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, v_idade):
        self.__idade = v_idade
        
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, v_peso):
        self.__peso = v_peso
    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, v_altura):
        self.__altura = v_altura
        
    def get_dados(self):
        return self.nome, self.idade, self.peso, self.altura
    
    def set_dados(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def get_csv(self):
        return f"{self.nome};{self.idade};{self.peso};{self.altura}"
    
    

julio = Pessoa("Julio")

print( julio.get_csv() )
    