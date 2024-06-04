from usuario import Usuario

class Empleado(Usuario):
    tipo_usuario=int
    dependencia=str
    año_ingreso=int

    def __init__(self, codigo=0,tipo_usuario=2):
        super().__init__(codigo)
        self.tipo_usuario=tipo_usuario

    def pedir_datos_empleado(self):
        while True:
            try:
                self.dependencia=input("Dependencia \n")
                self.año_ingreso=int(input("Ingresa el año de ingreso \n"))
                if self.año_ingreso>10000:
                    print("Error año de ingreso mayor a 10000")
                else:
                    break
            except:
                print("Error")