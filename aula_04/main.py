# Funçaõ com Retorno multiplo
def retorna_usuario_e_valor():
    return "Julio Pereira", 50.00


res = retorna_usuario_e_valor() # Tupla

# print(res)


## PROGRAMAÇÃO ORIENTADA A OBJETO


# ABSTRAÇÃO
# OBJETO

# PROPRIEDADE ou ATRIBUTO
# MÉTODOS (FUNÇÕES)

class Panela:
    pass

class Copo:
    def __init__(self): # CONSTRUTOR
        self.status = "Novo"

    # PROPRIEDADE COR
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, v_cor):
        self.__cor = v_cor
       
    # PROPRIEDADE TAMANHO 
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, v_tamanho):
        self.__tamanho = v_tamanho
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, v_status):
        self.__status = v_status
        
    def acao_cair(self):
        self.status = "Quebrado"
        


copo_americano = Copo()
copo_plastico = Copo()

copo_americano.cor = "Transparente"
copo_americano.tamanho = "250ML"
copo_americano.acao_cair()

copo_plastico.cor = "Azul"
copo_plastico.tamanho = "200ML"


print(f"Abstração: {Copo}")
print(f"Objeto: {copo_americano}")
print(f"(AMERICANO) Propriedade: {copo_americano.cor}")
print(f"(AMERICANO) Propriedade: {copo_americano.tamanho}")
print(f"(AMERICANO) Propriedade: {copo_americano.status}")
print("")
print(f"(PLASTICO) Propriedade: {copo_plastico.cor}")
print(f"(PLASTICO) Propriedade: {copo_plastico.tamanho}")
print(f"(PLASTICO) Propriedade: {copo_plastico.status}")

