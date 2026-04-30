from persistencia import Persistencia

class Arquivo(Persistencia):
    def __init__(self, tipo):
        super().__init__(tipo)
        
    def create(self, nome, local, data:list=None):
        return None
    
    def read(self):
        return None
    
    def update(self):
        return None
    
    def delete(self):
        return None
    

arquivo = Arquivo("arquivo")

