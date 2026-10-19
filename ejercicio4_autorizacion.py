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

combustible_disponible = int(print("ingrese la cantidad de combustible disponible: "))
combustible_llegar = int(print("ingrese la cantidad de combustible requerido para llegar: "))
combustible_regresar = int(print("ingrese la cantidad de de combustible requerido para regresar: "))
oxigeno_disponible = int(print("ingrese la cantidad de oxigeno disponible: "))
oxigeno_requerido = int(print("ingrese la cantidad de oxigeno requerido: "))
energia_diponible = int(print("ingrese la cantidad de energia disponible: "))
energia_requerida = int(print("ingrese la cantidad de energia requerida: "))
provisiones_disponibles = int(print("ingrese la cantidad de provisiones disponible: "))
provisiones_requeridas = int(print("ingrese la cantidad de provisiones requeridas: "))

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
    energia_diponible >= energia_requerida
    provisiones_disponibles >= energia_requerida):
    print ("lanzamiento autorizado")
elif:
    print ("lanzamiento denegado, la mision debe ser revisada")
    

