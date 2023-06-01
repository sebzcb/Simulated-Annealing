import random
from Comuna import Comuna

def crearComunas():
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
    algarrobo.comunasVecinas = []
    cartagena.comunasVecinas = []
    elQuisco.comunasVecinas = []
    elTabo.comunasVecinas = []
    sanAntonio.comunasVecinas = []
    santoDomingo.comunasVecinas = []
    catemu.comunasVecinas = []
    llayLlay.comunasVecinas = []
    panquehue.comunasVecinas = []
    putaendo.comunasVecinas = []
    sanFelipe.comunasVecinas = []
    santaMaria.comunasVecinas = []
    quilpue.comunasVecinas = []
    concon.comunasVecinas = []
    puchuncavi.comunasVecinas = []
    casablanca.comunasVecinas = []
    quintero.comunasVecinas = []
    valparaiso.comunasVecinas = []
    villaAlemana.comunasVecinas = []
    vinaDelMar.comunasVecinas = []

    #Se agregan las comunas a la lista de comunas
    comunas.extend([
        calleLarga, sanEsteban, rinconada, losAndes, cabildo, laLigua, papudo, petorca, zapallar, hijuelas,
        laCalera, laCruz, limache, nogales, olmue, quillota, algarrobo, cartagena, elQuisco, elTabo, sanAntonio,
        santoDomingo, catemu, llayLlay, panquehue, putaendo, sanFelipe, santaMaria, quilpue, concon, puchuncavi,
        casablanca,quintero,valparaiso,villaAlemana,vinaDelMar])

    return comunas

def mostrarComunas(comunas):
    for comuna in comunas :
        comuna.mostrarDatos()

comunas = crearComunas()
mostrarComunas(comunas)
#PROCESO simulated annealing

'''

Inicializar temperatura inicial
Inicializar temperatura parada
Inicializar el factor de enfriamiento

Establecer la solución actual como la solución inicial, actualiza arreglo comunas
Establecer el costo actual como el costo total de la solución actual

Mientras la temperatura actual sea mayor que temperatura de parada:
    Generar una solución vecina haciendo un movimiento aleatorio (SWAP)
    Calcular el costo de la solución vecina
    
    Calcular la diferencia de costos entre la solución vecina y la solución actual
    
    Si la solución vecina es mejor (tiene un costo menor):
        Aceptar la solución vecina como la nueva solución actual
        Actualizar el costo actual con el costo de la solución vecina
    Si no:
        Calcular la probabilidad de aceptación según el criterio de Metropolis
        Generar un número aleatorio entre 0 y 1
        
        Si el número aleatorio es menor o igual a la probabilidad de aceptación:
            Aceptar la solución vecina como la nueva solución actual
            Actualizar el costo actual con el costo de la solución vecina
    
    Reducir la temperatura multiplicándola por el factor de enfriamiento

Devolver la mejor solución encontrada

'''

