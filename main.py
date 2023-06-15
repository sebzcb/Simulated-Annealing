from MetodosComunas import *
import math
import random

#crear poblacion
comunas = MetodosComunas.crear() #se crean las comunas y la lista de comunas creada se retorna a variable comunas
#MetodosComunas.mostrar(comunas)

#inicializar variables control
temperaturaActual = 100
temperaturaFin = 0

#si el factor de enfriamiento es muy bajo, disminuye la temperatura muy rapido y por tanto cuando se hace el calculo de la probabilidad de 
# aceptacion muchas veces el numero es muy pequeño y ocurre errores, ej errores : 0.2
factorEnfriamiento = 0.9


print("Solucion inicial")
solucionActual = MetodosComunas.generarSolucionInicial(comunas) #actualiza la lista de comunas actual poniendo antenas de forma random, pero asegurando cobertura total.
MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)

print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")
costoSolucionActual = MetodosComunas.calcularCostoTotal(solucionActual)

historialSoluciones = []
iteraciones = 0
while iteraciones < 10 :
    #Generar una solución vecina haciendo un movimiento aleatorio (SWAP)
    solucionVecina = MetodosComunas.generarSolucionVecina(solucionActual)
    print("solucion vecina::::")
    MetodosComunas.mostrarDatosAntenasCobertura(solucionVecina)
    #Calcular el costo de la solución vecina
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
        print(f"e ** ( {dif} / {temperaturaActual})")
        probabilidadAceptacion = math.exp(-dif / temperaturaActual)
        print(f"prob. aceptacion = {probabilidadAceptacion}")
        #Generar un número aleatorio entre 0 y 1
        numeroRandom = random.random()

        #Si el número aleatorio es menor o igual a la probabilidad de aceptación:
        if(numeroRandom <= probabilidadAceptacion):
            #Aceptar la solución vecina como la nueva solución actual
            solucionActual = solucionVecina
            #Actualizar el costo actual con el costo de la solución vecina
            costoSolucionActual = costoSolucionVecina

            print(f"{numeroRandom} < {probabilidadAceptacion} Hay nueva solucion, costo {costoSolucionActual}")
            historialSoluciones.append(solucionActual)
        else:    
            print("No hay solucion nueva")
    iteraciones+=1
    temperaturaActual*=factorEnfriamiento

#sale del While
print(f"Iteracioness: {iteraciones}")


MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)
print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")

MetodosComunas.verificarDatosCorrectos(solucionActual)



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

