from material import Material
class Revista(Material):
    tipo_de_material=int
    issn=int
    volumen=int
    año_publicacion=int
    numero_publicacion=int

    def __init__(self, titulo="", asignatura_topografica="", numero_inventario=0, estado=1,coleccion=0, c_usuario = 0, fecha_devolucion="",tipo_de_material=3):
        super().__init__(titulo=titulo, asignatura_topografica=asignatura_topografica, numero_inventario=numero_inventario, estado=estado,coleccion=coleccion,c_usuario = 0,fecha_devolucion="")
        self.tipo_de_material=tipo_de_material

    def pedir_datos_h(self):
            self.editorial=input("editorial ")
            while True:
                try:
                    self.issn=int(input("ISSN "))
                    self.volumen=int(input("volumen "))
                    self.numero_publicacion=int(input("Numero de publicacion "))
                    self.año_publicacion=int(input("Año de publicacion "))
                    if self.año_publicacion>10000:
                        print("Error año de publicacion mayor a 10000")
                    else:
                        break
                except:
                    print("Error")