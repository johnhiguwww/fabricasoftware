from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self):
        """
        Defina na classe filha
        """
    def andar(self):
        """
        Defina na classe filha
        """

class Cachorro(IAnimal):
    def falar(self):
        print("AuAu")
    
    def andar(self):
        print("Ando com Quatro patas")

class Pessoa:

    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self.idade = idade
        self.__humano = True

    def fala_pessoa(self):
        print("Falando")
    
    def mostra_nome(self):
        print(self._nome)

#animal = IAnimal()
pingo = Cachorro()
pingo.andar()
pingo.falar()

humano = Pessoa("arthur", 25)

humano.fala_pessoa()
humano.mostra_nome()