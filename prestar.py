from datetime import date,timedelta
from estudiante import Estudiante
class Prestar():
    def fecha(self,dias_prestamo):
        while True:
            try:
                dia=int(input("ingresa el dia "))
                mes=int(input("ingresa el mes "))
                año=int(input("ingresa el año "))
                if 1 <= mes <= 12 and 1 <= dia <= 31 and año >= 0:
                    self.fecha_inicial=date(año,mes,dia)
                    fecha_final = self.fecha_inicial + timedelta(days=dias_prestamo)
                    fecha_final=str(fecha_final)
                    break
                else:
                    print("Error de fecha")
            except:
                print("Error ")
        return fecha_final