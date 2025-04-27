from app.models.huron import Huron
from app.models.boa_constrictor import Boa_Constrictor

class Guarderia():
    
    huron1=Huron("Frank",2,28,"Colombia",250000)
    huron2=Huron("Donald",1,15,"USA",200000)
    boa1=Boa_Constrictor("Jimmy",3,30,"Colombia",550000,2)
    boa2=Boa_Constrictor("Susi",5,80,"Brasil",850000,5)
    
    def alimentar_boa(self):
        try:
            res=Boa_Constrictor.comer_raton(self)
        except ValueError:
            print("La boa esta Llena!!!")
        except:
            print("Esta boa no existe!!!")
        else:
            print("Exito!!!")
        