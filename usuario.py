class Usuario():
    codigo=int

    def __init__(self,codigo=0):
        self.codigo=codigo

    def pedir_datos(self):
        while True:
            try:
                self.codigo=int(input("Ingresa el codigo \n"))
                break
            except:
                print("Error ")
