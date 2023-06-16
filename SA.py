import copy
import random
import MetodosComunas
import math

def generarSolucionInicial(comunas):
        coberturaTotal = False
        intentos = 0
        while not coberturaTotal:
            solucionInicial = copy.deepcopy(comunas)
            intentos += 1
            for comuna in solucionInicial:
                comuna.tieneAntena = random.choice([True, False])
                if comuna.tieneAntena:
                    comuna.tieneCobertura = True
                    MetodosComunas.actualizarCoberturaVecinos(comuna)
           
            coberturaTotal = MetodosComunas.verificarCoberturaTotal(solucionInicial)
        print(f"Intentos totales para generar solucion inicial: {intentos}")
        return solucionInicial

def generarSolucionVecina(comunas):
    tieneCoberturaTotal = False    

    # Mientras no se cumpla la cobertura total, sigue generando soluciones vecinas
    iteraciones = 0
    while not tieneCoberturaTotal:  
        # Copia la solución actual para modificarla        
        solucionVecina = copy.deepcopy(comunas)

        #devuelta a la solucion vecina.
        iteraciones+=1
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
            
        MetodosComunas.actualizarCoberturaAntenas(solucionVecina)
            #if MetodosComunas.verificarDatosCorrectos(solucionVecina,comunas):
        if MetodosComunas.verificarCoberturaTotal(solucionVecina):
            tieneCoberturaTotal = True
            # Verifica la cobertura de todas las comunas
    print(f"intentos para sol. vecina: {iteraciones}")
    return solucionVecina
    
#segun el criterio de metropolis
def criterioAceptacion(diferenciaCostos,temperaturaActual):
    print(f"e ** (-{diferenciaCostos}/{temperaturaActual})")
    
    # En caso que el numero sea demasiado pequeño y produzca errores se hace un try-except, evitando errores a nivel de ejecucion
    '''try:
        probabilidadAceptacion =  math.exp(-diferenciaCostos / temperaturaActual)
    except OverflowError:
        print("Provoco un overflow")
        probabilidadAceptacion = 0
    '''
    probabilidadAceptacion =  math.exp(-diferenciaCostos / temperaturaActual)
    
    #Generar un número aleatorio entre 0 y 1
    numeroRandom = random.random()
    if (numeroRandom <= probabilidadAceptacion):
        return True
    return False

def criterioTermino(iteraciones,iteracionesMax,temperaturaActual,temperaturaMinima):
    if iteraciones < iteracionesMax and temperaturaActual > temperaturaMinima :
        return False
    return True