class Comuna:

    ultimoId = 0 
    #Constructor de la clase
    def __init__(self, nombre, costo):
        Comuna.ultimoId+=1
        self.id = Comuna.ultimoId
        self.nombre = nombre
        self.costo = costo
        self.comunasVecinas = []
        self.tieneAntena = False 
        self.tieneCobertura = False
    
    
    # Metodos de la clase

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} ID: {self.id} COSTO: {self.costo}" )
        self.mostrarVecinos()

    def mostrarDatosAntenaCobertura(self):
        # Definir el ancho de cada columna
        anchoColumnaNombre = 20
        anchoColumnaAntena = 20
        
         #el nombre se alinea a la izquierda (<) en una columna de ancho definido por anchoColumnaNombre
        nombre = f"{self.nombre:<{anchoColumnaNombre}}"
        #el valor tieneAntena se alinea a la izquierda (:<) en una columna de ancho definido por anchoColumnaAntena, se usa str() para convertirlo a boolean
        antena = f"{str(self.tieneAntena):<{anchoColumnaAntena}}" 

        # Imprimir los datos alineados
        print(f"{nombre} {antena} {self.tieneCobertura}")

    def mostrarVecinos(self):
        vecinosString = ""
        for comunaVecina in self.comunasVecinas:
            vecinosString += comunaVecina.nombre + ", "
        vecinosString = vecinosString.rstrip(", ")  # Eliminar la última coma y espacio en blanco
        print("Comunas vecinas:", vecinosString)
        print()

    