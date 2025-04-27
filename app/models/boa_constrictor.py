from app.models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    
    def __init__(self, nombre, edad, peso, paisOrigen, impuestos,ratonesComidos:int):
        super().__init__(nombre, edad, peso, paisOrigen, impuestos)
        self.__ratonesComidos=ratonesComidos
        
    def get_ratonescomidos(self):
        return self.__ratonesComidos
    
    def set_ratonescomidos(self,ratonesComidos):
        
            self.__ratonesComidos=ratonesComidos
        
    
    def hacer_sonido(self):
        return "¡Tsss!"
    
    def comer_raton(self):
        if self.__ratonesComidos<=20:
            self.__ratonesComidos=self.__ratonesComidos+1
        else:
            raise ValueError("Demasiados Ratones!!!")
