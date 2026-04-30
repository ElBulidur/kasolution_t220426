
class Persistencia:
    def __init__(self, tipo):
        self.tipo = tipo
     
    def get_conection(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclase") 
        
    def create(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def read(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def update(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def delete(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")