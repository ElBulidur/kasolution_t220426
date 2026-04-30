

class Animal:
    def fazer_som(self):
        raise NotImplementedError("A subClasse tem que implementar fazer_som()!")

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!!"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!!"

    
animal = Animal()
# animal.fazer_som()

cachorro = Cachorro()
gato = Gato()

print(f"{Cachorro.__name__} ==> {cachorro.fazer_som()}")
print(f"{Gato.__name__} ==> {gato.fazer_som()}")