class Comuna:

    ultimoId = 0 
    def __init__(self, nombre, costo):

        self.id = Comuna.ultimoId+1
        self.nombre = nombre
        self.costo = costo
        self.comunasVecinas = []
        self.tieneAntena = False 
        self.tieneCobertura = False
