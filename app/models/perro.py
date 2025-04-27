from app.models.animal import Animal

class Perro(Animal):   
    # 1. constructores   
    def __init__(self, nombre:str, edad:int, peso: float, raza:str):
        super().__init__(nombre,edad, peso)
        self.__raza=raza

    # 2. Metodos (Comportamiento)
    
    def get_raza(self):
        return self.__raza
    
    def set_raza(self, nueva_raza):
        self.__raza=nueva_raza
    
    def emitir_sonido(self):
        return ("Guau Guau!!")