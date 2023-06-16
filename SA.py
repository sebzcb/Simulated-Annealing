import copy
import random
import MetodosComunas
import math

'''
Funcion que genera la solucion inicial recorriendo todas las comunas y poniendo antenas de forma random, se verifica que despues de generar la solucion
todas las comunas tengan cobertura, en caso que no se hace de nuevo el proceso hasta encontrar una solucion factible
'''

def generarSolucionInicial(comunas):
        coberturaTotal = False
        intentos = 0

        #Mientra no exista cobertura total
        while not coberturaTotal:
            solucionInicial = copy.deepcopy(comunas)
            intentos += 1

            #Recorre las comunas
            for comuna in solucionInicial:
                #Se elige aleatoriamente si poner o no una antena
                comuna.tieneAntena = random.choice([True, False])

                #Si se pone antena se pondra cobertura y cobertura a sus vecinos.
                if comuna.tieneAntena:
                    comuna.tieneCobertura = True
                    #Se pone cobertura a sus vecinos
                    MetodosComunas.actualizarCoberturaVecinos(comuna)
            
            #Se verifica si hay cobertura total, en caso que si retorna True a la variable coberturaTotal.
            coberturaTotal = MetodosComunas.verificarCoberturaTotal(solucionInicial)
        
        print(f"Intentos totales para generar solucion inicial: {intentos}")
        return solucionInicial

'''
Genera una solucion vecina usando el SWAP, intercambio entre antenas de dos comunas, uno tiene antena y el otro no. Se verifica que haya cobertura
total.
'''
def generarSolucionVecina(comunas):
    tieneCoberturaTotal = False    
    iteraciones = 0

    # Mientras no se cumpla la cobertura total, sigue generando soluciones vecinas
    while not tieneCoberturaTotal:  
        # Copia la solución actual para modificarla        
        solucionVecina = copy.deepcopy(comunas)

        iteraciones+=1
        #Selecciona dos comunas aleatoriamente,  tienen que ser distintos y uno tiene que tener antena y el otro no.
        comunasElegidas = False 
        while not comunasElegidas:
            comuna1 = random.choice(solucionVecina)
            comuna2 = random.choice(solucionVecina)
                #tienen que ser distintos Y uno tiene que tener antena y el otro no.
            if (comuna1.id != comuna2.id) and ( (comuna1.tieneAntena == True and comuna2.tieneAntena == False)  or (comuna1.tieneAntena == False and comuna2.tieneAntena == True)): 
                comunasElegidas=True
            
        # Realiza el swap entre las antenas de las dos comunas elegidas. 
        comuna1.tieneAntena, comuna2.tieneAntena = comuna2.tieneAntena, comuna1.tieneAntena
            
        #Actualiza la cobertura vecina ya que una comuna no tendra antena y la otra si.
        MetodosComunas.actualizarCoberturaAntenas(solucionVecina)

        #Si hay cobertura total se cambia el valor de tieneCoberturaTotal
        if MetodosComunas.verificarCoberturaTotal(solucionVecina):
            tieneCoberturaTotal = True

    print(f"intentos para sol. vecina: {iteraciones}")
    return solucionVecina
'''
Criterio de aceptacion segun el criterio de metropolis usando la formula e**(-diferenciaCostos/tempActual)
'''
def criterioAceptacion(diferenciaCostos,temperaturaActual):
    
    #print(f"e ** (-{diferenciaCostos}/{temperaturaActual})")
    '''
    # En caso que el numero sea demasiado pequeño y produzca errores se hace un try-except, evitando errores a nivel de ejecucion
    try:
        probabilidadAceptacion =  math.exp(-diferenciaCostos / temperaturaActual)
    except OverflowError:
        print("Provoco un overflow")
        probabilidadAceptacion = 0
    '''
    probabilidadAceptacion =  math.exp(-diferenciaCostos / temperaturaActual)
    
    #Generar un número aleatorio entre 0 y 1
    numeroRandom = random.random()

    #Si el numero random es menor a la probabilidad de aceptacion entonces acepta el criterio
    if (numeroRandom <= probabilidadAceptacion):
        return True
    return False
'''
Criterio de termino se basa en el numero de iteraciones max y la temperatura minima.
'''
def criterioTermino(iteraciones,iteracionesMax,temperaturaActual,temperaturaMinima):
    if iteraciones < iteracionesMax and temperaturaActual > temperaturaMinima :
        return False
    return True