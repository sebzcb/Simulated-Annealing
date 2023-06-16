from Comuna import Comuna

#Proceso que crea las comunas, asigna las comunas vecinas y retorna la lista de comunas creadas.
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
        
    #Se asignan las comunas vecinas
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

'''
Funcion que muestra los datos de nombre comuna, si tiene antena y  si tiene cobertura de todas las comunas. 
'''    
def mostrarDatosAntenasCobertura(comunas):
    print()
    # Encabezado de columnas
    encabezado_nombre = f"{'Nombre':<{20}}"
    encabezado_antena = f"{'Tiene Antena':<{20}}"
    encabezado_cobertura = f"{'Tiene Cobertura'}"

    print(f"{encabezado_nombre} {encabezado_antena} {encabezado_cobertura}")
    for comuna in comunas :
        comuna.mostrarDatosAntenaCobertura()
    
'''

'''
def actualizarCoberturaVecinos(comuna):
    for vecino in comuna.comunasVecinas:
        vecino.tieneCobertura = True

'''
Funcion que revisa que todas las comunas tengan cobertura, en caso que si retorna verdadero.
'''
def verificarCoberturaTotal(comunas):
    lista = []
    for comuna in comunas:
        if not comuna.tieneCobertura:
            lista.append(comuna)
            print(f"{comuna.nombre} no tiene cobertura ")

    if len(lista) == 0:
            return True
    return False

'''
Suma los costos de instalacion  en caso que en una comuna se haya puesto una antena y los retorna
'''
def calcularCostoTotal(comunas):
    costoTotal = 0
    for comuna in comunas:
        if comuna.tieneAntena:
            costoTotal += comuna.costo
    return costoTotal
'''
Cuenta la cantidad de antenas en la lista de comunas
'''
def calcularAntenas(comunas):
    antenas = 0
    for comuna in comunas:
        if comuna.tieneAntena:
            antenas+=1
    return antenas
'''
Primero reinicia el tieneCobertura en todas las comunas y luego ve todas las comunas que tengan antena desde el primero hasta el ultimo y 
les pone cobertura a sus vecinos y a si mismo.
'''
def actualizarCoberturaAntenas(comunas):
    #Reinicia el booleano tieneCobertura para no tener errores
    for c in comunas:
        c.tieneCobertura = False

    for comuna in comunas:
        if comuna.tieneAntena:
            comuna.tieneCobertura = True
            actualizarCoberturaVecinos(comuna)
            






            