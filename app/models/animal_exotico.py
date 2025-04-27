from abc import ABC, abstractmethod
from app.models.animal import Animal
from app.models.iAnimal import iAnimal

class Animal_Exotico(Animal,iAnimal):   
    # 1. constructores   
    def __init__(self, nombre:str, edad:int, peso: float, paisOrigen:str, impuestos:float):
        super().__init__(nombre,edad, peso)
        self.__pais_origen=paisOrigen
        self.__impuestos=impuestos

    # 2. Metodos (Comportamiento)
    
    def get_pais_origen(self):
        return self.__pais_origen
    
    def get_impuestos(self):
        return self.__impuestos
    
    def set_pais_origen(self, nueva_paisOrigen):
        self.__pais_origen=nueva_paisOrigen
        
    def set_impuestos(self,nuevo_impuesto):
        self.__impuestos=nuevo_impuesto
        
    def calcular_flete(self,impuestos,peso):
        return impuestos*peso