from abc import ABC, abstractmethod
#
# Clase padre: Contiene atributos en comun en diferentes clases
#
class Animal(ABC):
    
    def __init__(self,nombre:str,edad:int,peso:float):
        self._nombre=nombre
        self._edad=edad
        self._peso=peso
        
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    def get_peso(self):
        return self._peso
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre
    
    def set_edad(self, nueva_edad):
        self.__edad=nueva_edad
    
    def set_peso(self, nuevo_peso):
        self.__peso=nuevo_peso
    