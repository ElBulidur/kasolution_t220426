class Copo:
    def __init__(self, cor, tamanho, material):
        self.cor = cor
        self.tamanho = tamanho
        self.material = material
        self.status = "Novo"
        
    def acao_cair(self, impacto):
        if self.material == "Vidro":
            if impacto > 50:
                self.status = "Quebrou"
            else:
                self.status = "Trincou"
        elif self.material == "Plastico":
            self.status = "Amassou"
        else:
            pass
        
        
americano = Copo("Transparente", "250ML", "Vidro")
plastico = Copo("Azul", "200ML", "Plastico")

americano.acao_cair(40)
plastico.acao_cair(100)


print(f"Abstração: {Copo}")
print(f"Objeto: {americano}")
print(f"Objeto: {plastico}")
print(f"(AMERICANO) Propriedade: {americano.cor}")
print(f"(AMERICANO) Propriedade: {americano.tamanho}")
print(f"(AMERICANO) Propriedade: {americano.status}")
print("")
print(f"(PLASTICO) Propriedade: {plastico.cor}")
print(f"(PLASTICO) Propriedade: {plastico.tamanho}")
print(f"(PLASTICO) Propriedade: {plastico.status}")