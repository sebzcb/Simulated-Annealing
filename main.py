from MetodosComunas import *

#crear poblacion
comunas = MetodosComunas.crear() #se crean las comunas y la lista de comunas creada se retorna a variable comunas
#MetodosComunas.mostrar(comunas)

#inicializar variables control
temperaturaActual = 100
temperaturaFin = 10
factorEnfriamiento = 0.5 

print("Solucion inicial")
solucionActual = MetodosComunas.generarSolucionInicial(comunas) #actualiza la lista de comunas actual poniendo antenas de forma random, pero asegurando cobertura total.
MetodosComunas.mostrarDatosAntenasCobertura(solucionActual)
print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionActual)} Antenas: {MetodosComunas.calcularAntenas(solucionActual)}")
costoSolucionActual = MetodosComunas.calcularCostoTotal(solucionActual)

print("----------------")


while temperaturaActual > temperaturaFin:
    #Generar una solución vecina haciendo un movimiento aleatorio (SWAP)
    solucionVecina = MetodosComunas.generarSolucionVecina(comunas)

    #Calcular el costo de la solución vecina
    costoSolucionVecina = MetodosComunas.calcularCostoTotal(solucionVecina)
    
    MetodosComunas.mostrarDatosAntenasCobertura(solucionVecina) 
    print(f"Costo: {MetodosComunas.calcularCostoTotal(solucionVecina)} Antenas: {MetodosComunas.calcularAntenas(solucionVecina)}")

    if costoSolucionVecina < costoSolucionActual: 
        #Aceptar la solución vecina como la nueva solución actual
        solucionActual = solucionVecina
        #Actualizar el costo actual con el costo de la solución vecina
        costoSolucionActual = costoSolucionVecina
    else:
        #Calcular la probabilidad de aceptación según el criterio de Metropolis
        #Generar un número aleatorio entre 0 y 1
        
        #Si el número aleatorio es menor o igual a la probabilidad de aceptación:
            #Aceptar la solución vecina como la nueva solución actual
            #Actualizar el costo actual con el costo de la solución vecina
        continue
    temperaturaActual*=factorEnfriamiento

    print("Solucion Final: ")
    MetodosComunas.mostrar(solucionActual)
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

