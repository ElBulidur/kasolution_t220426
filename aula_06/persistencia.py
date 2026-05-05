from mimesis import Person, Address
from mimesis.locales import Locale


class Persistencia:
    def __init__(self, tipo):
        self.tipo = tipo
     
    def get_conection(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclase") 
        
    def create(self, data, destino=None):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def read(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def update(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
    def delete(self):
        raise NotImplementedError("Precisa fazer a implementação na Subclasse")
    
class ArquivoPersistencia(Persistencia):
    def __init__(self, tipo):
        super().__init__(tipo)
        
    def create(self
               , nome_arquivo:str, data:list = []
               , cabecalho=None, fake=False
               , qtd=10, extensao="txt"
            ):
        if fake:
            print("1 - Pessoa, 2 - Endereço")
            
            opcao = input("Qual mock vc quer(Escolha um numero): ")
            
            
            mock = None
            if opcao == "1":
                cabecalho="Nome_Completo"
                mock = Person(Locale.PT_BR)
                
                for _ in range(1, qtd+1):
                    data.append(mock.full_name())
            
            elif opcao == "2":
                cabecalho="Endereço_Completo"
                mock = Address(Locale.PT_BR)
                
                for _ in range(1, qtd+1):
                    data.append(mock.address())
            else:
                print("Ops! errou!")
                
            
        with open(nome_arquivo, "w") as arq:
            if cabecalho:
                arq.write(cabecalho+"\n")
            
            for item in data:
                arq.write(item+"\n")
                
    def read(self, arquivo):
        
        with open(arquivo, "r") as arq:
            res = arq.readlines()
            
        return res
    
    def update(self, arquivo, antigo_dado, novo_dado):
        
        partes = arquivo.split(".")
        
        arquivo_atualizado = f"{partes[0]}_atualizado.{partes[1]}"
        
        with open(arquivo, "r") as arq:
                res = arq.readlines()
        
        novo_data = []
        
        for linha in res:
            if linha != antigo_dado:
                novo_data.append(linha)
            else:
                novo_data.append(novo_dado)
                
        with open(arquivo_atualizado, "w") as arq:
            
            for item in novo_data:
                arq.write(item)
                
        print("Arquivo criado com atualização.")
                          
    def delete(self, arquivo, dado_deletar):
        
        with open(arquivo, "r") as arq:
                res = arq.readlines()
        
        novo_data = []
        
        for linha in res:
            if linha != dado_deletar:
                novo_data.append(linha)
                
        with open(arquivo, "w") as arq:
            
            for item in novo_data:
                arq.write(item)
                
        print("Dado deletado do arquivo com sucesso.")
            
class DBPersistencia(Persistencia):
    def __init__(self, tipo):
        super().__init__(tipo)
        
    