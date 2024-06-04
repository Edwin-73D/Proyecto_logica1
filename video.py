from material import Material
class Video(Material):
    tipo_de_material=int
    productor=str
    director=str
    año_grabacion=int
    genero=int

    def __init__(self, titulo="", asignatura_topografica="", numero_inventario=0, estado=1,coleccion=0, c_usuario = 0,fecha_devolucion="",tipo_de_material=2):
        super().__init__(titulo=titulo, asignatura_topografica=asignatura_topografica, numero_inventario=numero_inventario, estado=estado,coleccion=coleccion, c_usuario = 0, fecha_devolucion="")
        self.tipo_de_material=tipo_de_material

    def pedir_datos_h(self):
        self.productor=input("productor ")
        self.director=input("director ")
        while True:
            try:
                self.año_grabacion=int(input("año de grabacion "))
                if self.año_grabacion>10000:
                    print("Error año de grabacion mayor a 10000")
                else:
                    genero=int(input("1) para documental \n2) para comedia \n3) para terror \n4)para accion\n"))
                    match genero:
                        case 1:
                            self.genero=genero
                            break
                        case 2:
                            self.genero=genero
                            break
                        case 3:
                            self.genero=genero
                            break
                        case 4:
                            self.genero=genero
                            break
                        case _: print("Error")
            except:
                print("Error ")