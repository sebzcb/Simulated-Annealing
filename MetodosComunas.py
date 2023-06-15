from Comuna import Comuna
import random

class MetodosComunas:

    #Proceso crear comunas, asignar comunas vecinas y retornar lista de comunas creadas.
    def crear():
        comunas = []

        #Se crean las comunas junto al costo de poner antena, el id se pone automaticamente.
        calleLarga = Comuna("Calle larga",1)
        sanEsteban = Comuna("San Esteban",1.5)
        rinconada = Comuna("Rinconada",1.2)
        losAndes = Comuna("Los andes",2)
        cabildo = Comuna("Cabildo",3)
        laLigua = Comuna("La ligua",2)
        papudo = Comuna("Papudo",1)
        petorca = Comuna("Petorca",1)
        zapallar = Comuna("Zapallar",3)
        hijuelas = Comuna("Hijuelas",4)
        laCalera = Comuna("La Calera",3)
        laCruz = Comuna("La Cruz",3)
        limache = Comuna("Limache",2)
        nogales = Comuna("Nogales",2.5)
        olmue = Comuna("Olmue",1.5)
        quillota = Comuna("Quillota",2)
        algarrobo = Comuna("Algarrobo",2)
        cartagena = Comuna("Cartagena",3)
        elQuisco = Comuna("El Quisco",2)
        elTabo = Comuna("El Tabo",2)
        sanAntonio = Comuna("San Antonio",3)
        santoDomingo = Comuna("Santo Domingo", 2)
        catemu = Comuna("Catemu", 3)
        llayLlay = Comuna("Llay-Llay", 3)
        panquehue = Comuna("Panquehue", 1)
        putaendo = Comuna("Putaendo", 2.5)
        sanFelipe = Comuna("San Felipe", 2)
        santaMaria = Comuna("Santa Maria", 3.5)
        quilpue = Comuna("Quilpue", 2)
        concon = Comuna("Concon", 1.5)
        puchuncavi = Comuna("Puchuncavi", 2)
        casablanca = Comuna("Casablanca", 3)
        quintero = Comuna("Quintero", 3.5)
        valparaiso = Comuna("Valparaiso", 2)
        villaAlemana = Comuna("Villa Alemana", 2.5)
        vinaDelMar = Comuna("Viña del Mar", 1.5)
        
        #Se ponen las comunas vecinas
        calleLarga.comunasVecinas = [losAndes, sanFelipe, rinconada] 
        sanEsteban.comunasVecinas = [losAndes, santaMaria,putaendo]
        rinconada.comunasVecinas = [calleLarga,losAndes,sanFelipe,rinconada]
        losAndes.comunasVecinas = [sanEsteban,rinconada,sanFelipe,santaMaria]
        cabildo.comunasVecinas = [petorca,laLigua,nogales,catemu,putaendo] #existe la posibilidad que este san felipe
        laLigua.comunasVecinas = [papudo,zapallar,nogales,cabildo,petorca]
        papudo.comunasVecinas = [laLigua,zapallar]
        petorca.comunasVecinas = [laLigua,cabildo]
        zapallar.comunasVecinas = [papudo,laLigua,nogales,puchuncavi]
        hijuelas.comunasVecinas = [llayLlay,catemu,nogales,laCalera,laCruz,quillota,olmue]
        laCalera.comunasVecinas = [hijuelas,nogales,laCruz,quillota]
        laCruz.comunasVecinas = [hijuelas,laCalera,nogales,puchuncavi,quillota]
        limache.comunasVecinas = [olmue,quillota,concon,quilpue,villaAlemana] #existe la posibilidad de agregar otra comuna
        nogales.comunasVecinas = [cabildo,laLigua,zapallar,puchuncavi,laCruz,laCalera,hijuelas,catemu]
        olmue.comunasVecinas = [hijuelas, quillota,limache,quilpue]
        quillota.comunasVecinas = [hijuelas,laCalera,laCruz,puchuncavi,quintero,concon,limache,olmue]
        algarrobo.comunasVecinas = [casablanca,elQuisco]
        cartagena.comunasVecinas = [casablanca,elTabo,sanAntonio]
        elQuisco.comunasVecinas = [algarrobo,casablanca,elTabo]
        elTabo.comunasVecinas = [elQuisco,casablanca,cartagena]
        sanAntonio.comunasVecinas = [cartagena,santoDomingo]
        santoDomingo.comunasVecinas = [sanAntonio]
        catemu.comunasVecinas = [cabildo,nogales,hijuelas,llayLlay,panquehue,sanFelipe]
        llayLlay.comunasVecinas = [hijuelas,catemu,panquehue,rinconada]
        panquehue.comunasVecinas = [catemu,llayLlay,rinconada,sanFelipe]
        putaendo.comunasVecinas = [cabildo,catemu,sanFelipe,santaMaria,sanEsteban]
        sanFelipe.comunasVecinas = [cabildo,catemu,panquehue,rinconada,calleLarga,losAndes,santaMaria,putaendo]
        santaMaria.comunasVecinas = [putaendo,sanFelipe,losAndes,sanEsteban]
        quilpue.comunasVecinas = [olmue,limache,villaAlemana,concon,vinaDelMar,valparaiso,casablanca]
        concon.comunasVecinas = [quintero,quillota,limache,quilpue,vinaDelMar]
        puchuncavi.comunasVecinas = [zapallar,nogales,laCruz,quillota,quintero]
        casablanca.comunasVecinas = [valparaiso,quilpue,algarrobo,cartagena,elQuisco,elTabo]
        quintero.comunasVecinas = [puchuncavi,quillota,concon] ###
        valparaiso.comunasVecinas = [vinaDelMar,quilpue,casablanca]
        villaAlemana.comunasVecinas = [limache,quilpue]
        vinaDelMar.comunasVecinas = [concon,quilpue,valparaiso] ###

        #Se agregan las comunas a la lista de comunas
        comunas.extend([
            calleLarga, sanEsteban, rinconada, losAndes, cabildo, laLigua, papudo, petorca, zapallar, hijuelas,
            laCalera, laCruz, limache, nogales, olmue, quillota, algarrobo, cartagena, elQuisco, elTabo, sanAntonio,
            santoDomingo, catemu, llayLlay, panquehue, putaendo, sanFelipe, santaMaria, quilpue, concon, puchuncavi,
            casablanca,quintero,valparaiso,villaAlemana,vinaDelMar])

        return comunas
    
    def mostrar(comunas):
        for comuna in comunas :
            comuna.mostrarDatos()
    
    def mostrarDatosAntenasCobertura(comunas):
        print()
        # Encabezado de columnas
        encabezado_nombre = f"{'Nombre':<{20}}"
        encabezado_antena = f"{'Tiene Antena':<{20}}"
        encabezado_cobertura = f"{'Tiene Cobertura'}"

        print(f"{encabezado_nombre} {encabezado_antena} {encabezado_cobertura}")
        for comuna in comunas :
            comuna.mostrarDatosAntenaCobertura()
    
    def actualizarCoberturaVecinos(comuna):
        for vecino in comuna.comunasVecinas:
            vecino.tieneCobertura = True

    
    def verificarCoberturaTotal(comunas):
        for comuna in comunas:
            if not comuna.tieneCobertura:
                return False
        return True
    
    def generarSolucionInicial(comunas):
        solucionInicial = comunas.copy()

        coberturaTotal = False
        intentos = 0
        while not coberturaTotal:
            intentos+=1
            for comuna in solucionInicial:
                comuna.tieneAntena = random.choice([True, False])
                if comuna.tieneAntena:
                    comuna.tieneCobertura = True
                    MetodosComunas.actualizarCoberturaVecinos(comuna)
            coberturaTotal = MetodosComunas.verificarCoberturaTotal(solucionInicial)
        print(f"Intentos totales para generar solucion inicial: {intentos}")
        return solucionInicial

    
    def calcularCostoTotal(comunas):
        costoTotal = 0
        for comuna in comunas:
            if comuna.tieneAntena:
                costoTotal += comuna.costo
        return costoTotal
    
    def calcularAntenas(comunas):
        antenas = 0
        for comuna in comunas:
            if comuna.tieneAntena:
                antenas+=1
        return antenas
    
    def generarSolucionVecina(comunas):
        # Copia la solución actual para modificarla
        solucionVecina = comunas.copy()  

        tieneCoberturaTotal = False    
        # Mientras no se cumpla la cobertura total, sigue generando soluciones vecinas
        while not tieneCoberturaTotal:
            #Selecciona dos comunas aleatoriamente,  tienen que ser distintos y uno tiene que tener antena y el otro no.
            comunasElegidas = False 
            while not comunasElegidas:
                comuna1 = random.choice(solucionVecina)
                comuna2 = random.choice(solucionVecina)
                #tienen que ser distintos Y uno tiene que tener antena y el otro no.
                if (comuna1.id != comuna2.id) and ( (comuna1.tieneAntena == True and comuna2.tieneAntena == False)  or (comuna1.tieneAntena == False and comuna2.tieneAntena == True)): 
                    comunasElegidas=True
            
            # Realiza el swap entre las antenas de las dos comunas, 
            comuna1.tieneAntena, comuna2.tieneAntena = comuna2.tieneAntena, comuna1.tieneAntena
            print(f"Comuna1 elegida: {comuna1.nombre} tieneAntena : {comuna1.tieneAntena} costo: {comuna1.costo}")
            print(f"Comuna 2 elegida:{comuna2.nombre} tieneAntena : {comuna2.tieneAntena} costo: {comuna2.costo}")
            # Verifica la cobertura de todas las comunas
            tieneCoberturaTotal = MetodosComunas.verificarCoberturaTotal(solucionVecina)
        
        return solucionVecina
