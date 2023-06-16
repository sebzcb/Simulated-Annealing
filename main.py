import MetodosComunas
import time
import SA

def verHistorial(historialSoluciones):
        iteracion = 1
        for solucion in historialSoluciones:
            print(f"{iteracion}. N° antenas: {MetodosComunas.calcularAntenas(solucion)} Costo : {MetodosComunas.calcularCostoTotal(solucion)}")
            iteracion+=1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = MetodosComunas.calcularCostoTotal(arr[len(arr) // 2])
    left = []
    middle = []
    right = []
    for x in arr:
        costo = MetodosComunas.calcularCostoTotal(x)
        if costo < pivot:
            left.append(x)
        elif costo == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quicksort(left) + middle + quicksort(right)
def calcularMediaCostos(historialSoluciones):
    sumaCosto = 0 
    for solucion in historialSoluciones :
        sumaCosto+= MetodosComunas.calcularCostoTotal(solucion)
    return sumaCosto/len(historialSoluciones)

#calcula desviacion estandar del historial solucione, cada solucion es una  lista de comunas con una combinacion de antenas.
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

#crear poblacion
comunas = MetodosComunas.crear() #se crean las comunas y la lista de comunas creada se retorna a variable comunas
#MetodosComunas.mostrar(comunas)

#inicializar variables control
temperaturaActual = 500
temperaturaMinima = 0.001
iteracionesMax = 10

#si el factor de enfriamiento es muy bajo, disminuye la temperatura muy rapido y por tanto cuando se hace el calculo de la probabilidad de 
# aceptacion muchas veces el numero es muy pequeño y ocurre errores, ej errores : 0.2
factorEnfriamiento = 0.97

print(" Solucion Inicial ")
solucionActual = SA.generarSolucionInicial(comunas) #actualiza la lista de comunas actual poniendo antenas de forma random, pero asegurando cobertura total.
MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)

print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")

costoSolucionActual = MetodosComunas.calcularCostoTotal(solucionActual)
historialSoluciones = []
iteraciones = 0

while not SA.criterioTermino(iteraciones,iteracionesMax,temperaturaActual,temperaturaMinima) :
    #Generar una solución vecina haciendo un movimiento aleatorio (SWAP)
    solucionVecina = SA.generarSolucionVecina(solucionActual)
    costoSolucionVecina = MetodosComunas.calcularCostoTotal(solucionVecina)
    
    #MetodosComunas.mostrarDatosAntenasCobertura(solucionVecina) 
    print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionVecina)} Antenas: {MetodosComunas.calcularAntenas(solucionVecina)}")
    print(f"iteracion:{iteraciones}")
    if costoSolucionVecina < costoSolucionActual: 
        #Aceptar la solución vecina como la nueva solución actual
        solucionActual = solucionVecina
        #Actualizar el costo actual con el costo de la solución vecina
        costoSolucionActual = costoSolucionVecina
        historialSoluciones.append(solucionActual)
    else:
        #Calcular la probabilidad de aceptación según el criterio de Metropolis (e ** (-diferenciaCostos / temp. Actual))
        diferenciaCostos = costoSolucionActual- costoSolucionVecina        

        #Si el número aleatorio es menor o igual a la probabilidad de aceptación:
        if(SA.criterioAceptacion(diferenciaCostos,temperaturaActual)):
            #Aceptar la solución vecina como la nueva solución actual
            solucionActual = solucionVecina
            #Actualizar el costo actual con el costo de la solución vecina
            costoSolucionActual = costoSolucionVecina
            historialSoluciones.append(solucionActual)

    iteraciones+=1
    temperaturaActual*=factorEnfriamiento
    
print(f"Iteracioness: {iteraciones}")

MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)
print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")

verHistorial(historialSoluciones)
ordenado = quicksort(historialSoluciones)
verHistorial(ordenado)

print(f"Mejor solucion : {MetodosComunas.calcularCostoTotal(ordenado[0])}")

media = calcularMediaCostos(historialSoluciones)
print(f"Costo promedio por instalar antena :{media} D.E = {calcularDesviacionEstandar(historialSoluciones,media)}")
print(f"{time.time()} segundos ")


