from usuario import Usuario

class Estudiante(Usuario):
    tipo_usuario=int
    programa_academico=str

    def __init__(self, codigo=0,tipo_usuario=1):
        super().__init__(codigo)
        self.tipo_usuario=tipo_usuario

    def pedir_datos_estudiante(self):
        while True:
            try:
                self.programa_academico=input(f"Ingresa tu programa academico \n")
                break
            except:
                print("Error ")
