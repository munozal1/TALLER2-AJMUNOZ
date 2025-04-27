from app.models.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    
    def __init__(self, nombre, edad, peso, paisOrigen, impuestos):
        super().__init__(nombre, edad, peso, paisOrigen, impuestos)
        
    def hacer_sonido(self):
        return "¡Eek Eek!"
