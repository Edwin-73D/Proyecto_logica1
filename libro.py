from material import Material
class Libro(Material):
    tipo_de_material=int
    autor=str
    isbn=str
    editorial=str
    numero_edicion=int

    def __init__(self, titulo="", asignatura_topografica="", numero_inventario=0, estado=1,coleccion=0, c_usuario = 0, fecha_devolucion="",tipo_de_material=1):
        super().__init__(titulo=titulo, asignatura_topografica=asignatura_topografica, numero_inventario=numero_inventario, estado=estado,coleccion=coleccion, c_usuario = 0, fecha_devolucion="")
        self.tipo_de_material=tipo_de_material


    def pedir_datos_h(self):
        self.autor=input("Ingresa el nombre del autor \n")
        self.isbn=input("ISBN \n")
        self.editorial=input("Editorial \n")
        while True:
            try:
                self.numero_edicion=int(input("Numero de edicion \n"))
                break
            except:
                print("Ingresa un numero")
