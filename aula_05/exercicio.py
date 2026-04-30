"""
    Laboratório 1

    Escrever uma classe chamada Pessoa. Esta classe deve ter as propriedades:
        => Nome;
        => Idade;
        => Peso;
        => Altura.

    Definir também os seguintes métodos:
        => get_dados(): usado para retornar os dados da pessoa;
        => set_dados(): usado para atribuir todos os dados da pessoa;
        => get_csv(): usado para retornar os dados da pessoa separados por ponto-e-vírgula (;) com o propósito
        de gerar um arquivo no formato CSV (o arquivo não será contemplado neste exercício).

    Incluir também um construtor capaz de receber valores para todas as propriedades, porém sendo apenas o nome
    da pessoa obrigatório.
"""

class Pessoa:
    def __init__(self, v_nome, v_idade=None, v_peso=None, v_altura=None):
        self.nome = v_nome
        self.idade = v_idade
        self.peso = v_peso
        self.altura = v_altura
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, v_nome):
        self.nome = v_nome
        
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, v_idade):
        self.idade = v_idade
        
        
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, v_peso):
        self.peso = v_peso
        
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, v_altura):
        self.altura = v_altura
        
    def get_dados(self):
        return f"Nome: {self.nome}, idade: {self.idade}\
            , peso: {self.peso}, altura: {self.altura}"
            
    def set_dados(self, idade, peso, altura):
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def get_csv(self):
        return f"{self.nome};{self.idade};{self.peso};{self.altura}"
    
    
        
    
        