import MetodosComunas
import time
import SA
'''
Esta funcion almacena las soluciones obtenidas durante la ejecucion del algoritmo, cada solucion representa una lista de comunas en la que cada
comuna puede o no tener una antena y tener o no cobertura.
'''
def verHistorial(historialSoluciones):
        iteracion = 1
        for solucion in historialSoluciones:
            print(f"{iteracion}. N° antenas: {MetodosComunas.calcularAntenas(solucion)} Costo : {MetodosComunas.calcularCostoTotal(solucion)}")
            iteracion+=1

'''
Es el algoritmo de ordenamiento utilizado donde se se elige un pivote que esta ubicado en la mitad y despues se ve si la solucion elegida tiene 
menor, igual o mayor costo que el pivote. Funciona de forma recursiva.
'''
def quicksort(historialSoluciones):
    if len(historialSoluciones) <= 1:
        return historialSoluciones
    pivot = MetodosComunas.calcularCostoTotal(historialSoluciones[len(historialSoluciones) // 2])
    left = []
    middle = []
    right = []
    for listaComunas in historialSoluciones:
        costo = MetodosComunas.calcularCostoTotal(listaComunas)
        if costo < pivot:
            left.append(listaComunas)
        elif costo == pivot:
            middle.append(listaComunas)
        else:
            right.append(listaComunas)
    return quicksort(left) + middle + quicksort(right)

'''
Funcion que retorna el promedio de costos de las soluciones generadas.
'''

def calcularMediaCostos(historialSoluciones):
    sumaCosto = 0 
    for solucion in historialSoluciones :
        sumaCosto+= MetodosComunas.calcularCostoTotal(solucion)
    return sumaCosto/len(historialSoluciones)
'''
Calcula la desviacion estandar del historial de soluciones usando la formula.
'''
def calcularDesviacionEstandar(historialSoluciones,media):
    # Calculamos la suma de los cuadrados de las diferencias con la media    
    sumaCuadrados = 0
    for listaComunas in historialSoluciones:
        sumaCuadrados += (MetodosComunas.calcularCostoTotal(listaComunas) - media) ** 2

    # Calculamos la varianza dividiendo la suma de los cuadrados entre el tamaño de la lista
    varianza = sumaCuadrados / (len(historialSoluciones)-1)

    # Calculamos la desviación estándar como la raíz cuadrada de la varianza
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar

#Se crea la lista de comunas con los datos correspondientes y se retorna a la variable comunas
comunas = MetodosComunas.crear() 

#inicializar variables control
temperaturaActual = 500
temperaturaMinima = 0.001
iteracionesMax = 10
#si el factor de enfriamiento es muy bajo, disminuye la temperatura muy rapido y por tanto cuando se hace el calculo de la probabilidad muy pequeño
#puede producir errores si es muy bajo
factorEnfriamiento = 0.97

#Se genera la solucion inicial
solucionActual = SA.generarSolucionInicial(comunas) 
MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)

print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")


costoSolucionActual = MetodosComunas.calcularCostoTotal(solucionActual)
historialSoluciones = []
iteraciones = 0

#Mientras no ocurra el criterio de termino
while not SA.criterioTermino(iteraciones,iteracionesMax,temperaturaActual,temperaturaMinima) :

    #Genera una solución vecina haciendo un movimiento aleatorio (SWAP) entre antenas de dos comunas.
    solucionVecina = SA.generarSolucionVecina(solucionActual)
    costoSolucionVecina = MetodosComunas.calcularCostoTotal(solucionVecina)
    
    print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionVecina)} Antenas: {MetodosComunas.calcularAntenas(solucionVecina)}")
    print(f"iteracion:{iteraciones}")

    if costoSolucionVecina < costoSolucionActual: 
        #Acepta la solución vecina como la nueva solución actual
        solucionActual = solucionVecina
        
        #Actualiza el costo actual con el costo de la solución vecina
        costoSolucionActual = costoSolucionVecina

        historialSoluciones.append(solucionActual)
    else:
        diferenciaCostos = costoSolucionActual- costoSolucionVecina        
        
        #Si se acepta segun el criterio de aceptacion usado (criterio de metropolis) se acepta como solucion tambien.
        if(SA.criterioAceptacion(diferenciaCostos,temperaturaActual)):
            #Acepta la solución vecina como la nueva solución actual
            solucionActual = solucionVecina
            #Actualiza el costo actual con el costo de la solución vecina
            costoSolucionActual = costoSolucionVecina
            
            historialSoluciones.append(solucionActual)

    iteraciones+=1
    #Actualiza la temperatura actual
    temperaturaActual*=factorEnfriamiento


#Resultados finales
print(f"Iteraciones totales: {iteraciones}")
MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)
print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")

#Se ordena el historial de menor a mayor usando el quicksort
historialOrdenado = quicksort(historialSoluciones)
verHistorial(historialOrdenado)

print(f"Mejor solucion encontrada: {MetodosComunas.calcularCostoTotal(historialOrdenado[0])}")

media = calcularMediaCostos(historialSoluciones)
print(f"Costo promedio por instalar antena :{media} D.E = {calcularDesviacionEstandar(historialSoluciones,media)}")
print(f"{time.time()} segundos ")


