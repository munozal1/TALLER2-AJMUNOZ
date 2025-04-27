from app.models.animal import Animal

class Gato(Animal):
    
    def __init__(self,nombre:str,color:str,edad: int,peso: float):
        super().__init__(nombre,edad, peso)
        self.__color=color
        
    def get_color(self):
        return self.__color
    
    def set_color(self,nuevo_color):
        self.__color=nuevo_color
        
    def emitir_sonido(self):
        return ("Miau, Miau!")