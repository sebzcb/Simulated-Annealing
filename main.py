from MetodosComunas import *
import math
import random
import time

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


#crear poblacion
comunas = MetodosComunas.crear() #se crean las comunas y la lista de comunas creada se retorna a variable comunas
#MetodosComunas.mostrar(comunas)

#inicializar variables control
temperaturaActual = 100
temperaturaFin = 0

#si el factor de enfriamiento es muy bajo, disminuye la temperatura muy rapido y por tanto cuando se hace el calculo de la probabilidad de 
# aceptacion muchas veces el numero es muy pequeño y ocurre errores, ej errores : 0.2
factorEnfriamiento = 0.9
iteracionesMax = 100
print("Solucion inicial")
solucionActual = MetodosComunas.generarSolucionInicial(comunas) #actualiza la lista de comunas actual poniendo antenas de forma random, pero asegurando cobertura total.
MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)

print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")
costoSolucionActual = MetodosComunas.calcularCostoTotal(solucionActual)

historialSoluciones = []
iteraciones = 0
while iteraciones < iteracionesMax :
    #Generar una solución vecina haciendo un movimiento aleatorio (SWAP)
    solucionVecina = MetodosComunas.generarSolucionVecina(solucionActual)
    costoSolucionVecina = MetodosComunas.calcularCostoTotal(solucionVecina)
    
    #MetodosComunas.mostrarDatosAntenasCobertura(solucionVecina) 
    print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionVecina)} Antenas: {MetodosComunas.calcularAntenas(solucionVecina)}")
    
    if costoSolucionVecina < costoSolucionActual: 
        #Aceptar la solución vecina como la nueva solución actual
        solucionActual = solucionVecina
        #Actualizar el costo actual con el costo de la solución vecina
        costoSolucionActual = costoSolucionVecina
        print(f"entro if Hay nueva solucion, costo: {costoSolucionActual}")
        historialSoluciones.append(solucionActual)
        
    else:
        #Calcular la probabilidad de aceptación según el criterio de Metropolis (e ** (-diferenciaCostos / temp. Actual))
        dif = costoSolucionActual-costoSolucionVecina
        probabilidadAceptacion = math.exp(-dif / temperaturaActual)
        #Generar un número aleatorio entre 0 y 1
        numeroRandom = random.random()

        #Si el número aleatorio es menor o igual a la probabilidad de aceptación:
        if(numeroRandom <= probabilidadAceptacion):
            #Aceptar la solución vecina como la nueva solución actual
            solucionActual = solucionVecina
            #Actualizar el costo actual con el costo de la solución vecina
            costoSolucionActual = costoSolucionVecina
            historialSoluciones.append(solucionActual)

    iteraciones+=1
    temperaturaActual*=factorEnfriamiento
    

#sale del While
print(f"Iteracioness: {iteraciones}")

MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)
print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")

print(f"largo historial:{len(historialSoluciones)}")
print(f"temp : {temperaturaActual}")

verHistorial(historialSoluciones)
ordenado = quicksort(historialSoluciones)
verHistorial(ordenado)

print(f"Mejor solucion : {MetodosComunas.calcularCostoTotal(ordenado[0])}")
print(f"{time.time()} segundos ")




