class Comuna:

    ultimoId = 0 
    def __init__(self, nombre, costo):
        Comuna.ultimoId+=1
        self.id = Comuna.ultimoId
        self.nombre = nombre
        self.costo = costo
        self.comunasVecinas = []
        self.tieneAntena = False 
        self.tieneCobertura = False
      

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print("Comunas vecinas:")
        for comunaVecina in self.comunasVecinas:
            print(comunaVecina.nombre)
        print()