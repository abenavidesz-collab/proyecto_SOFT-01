#Nombre del archivo (ejercicio4_autorizacion.py)
#Curso (SOFT-01)
#Nombres de los integrantes (Andres Benavides y Daniel Fezta)
#Fecha viernes 16 de octubre

#Descripción
#La agencia necesita realizar una verificación general antes de permitir el lanzamiento. Se debe
#utilizar una estructura condicional doble sin condicionales anidadas.
#Datos solicitados
#• Combustible disponible.
#• Combustible requerido para llegar al destino.
#• Combustible requerido para regresar.
#• Oxígeno disponible y oxígeno requerido.
#• Energía disponible y energía requerida.
#• Provisiones disponibles y provisiones requeridas.

COMBUSTIBLE_ADICIONAL = 10

combustible_disponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustible_llegar = int(input("Ingrese la cantidad de combustible requerido para llegar: "))
combustible_regresar = int(input("Ingrese la cantidad de combustible requerido para regresar: "))
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
energia_disponible = int(input("Ingrese la cantidad de energía disponible: "))
energia_requerida = int(input("Ingrese la cantidad de energía requerida: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponible: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

#Cálculo requerido
#Combustible total requerido = combustible de ida + combustible de regreso + 10
#Regla de autorización
#La misión únicamente podrá ser autorizada cuando se cumplan todas las condiciones siguientes:
#• El combustible disponible es mayor o igual que el combustible total requerido.
#• El oxígeno disponible es mayor o igual que el requerido.
#• La energía disponible es mayor o igual que la requerida.
#• Las provisiones disponibles son mayores o iguales que las requeridas.

combustible_requerido = combustible_llegar + combustible_regresar + COMBUSTIBLE_ADICIONAL

if (combustible_disponible >= combustible_requerido and 
    oxigeno_disponible >= oxigeno_requerido and 
    energia_disponible >= energia_requerida and
    provisiones_disponibles >= provisiones_requeridas):
    print ("Lanzamiento autorizado")
else:
    print ("Lanzamiento denegado, la misión debe ser revisada")


