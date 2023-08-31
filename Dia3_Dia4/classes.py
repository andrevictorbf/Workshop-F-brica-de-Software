"""classe abstrata"""
from abc import ABC, abstractmethod

class IAnimal(ABC):
    
    @abstractmethod
    def falar(self): #self instancia criada
        """Defina na classe filha"""
    @abstractmethod
    def andar(self): 
     """Defina na classe filha"""
class Cachorro (IAnimal):
    def falar(self):
        print("auau")
    def andar(self):
        print("andar com 4 patas")
    def rolar(self):
        print("Rolando")
            
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
        self.__humano = True #privado 
    def fala_pessoa (self):
        print("Falando")

pingo = Cachorro()
pingo.falar()
pingo.andar()
pingo.rolar()