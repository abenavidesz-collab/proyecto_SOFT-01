#Nombre del archivo (ejercicio3_verificacion.py)
#Curso (SOFT-01)
#Nombres de los integrantes (Andres Benavides y Daniel Fezta)
#Fecha viernes 16 de octubre

#Ejercicio 3: Verificación del soporte para la tripulación
#Descripción
#Antes de autorizar la misión, es necesario verificar si existen suficientes recursos para mantener a
#toda la tripulación durante el viaje. Este ejercicio debe utilizar una estructura condicional doble.
#Datos solicitados
#• Cantidad de oxígeno disponible.
#• Cantidad de oxígeno requerido.
#• Cantidad de provisiones disponibles.
#• Cantidad de provisiones requeridas.

oxigeno_disponible = int(input("ingrese la catidad de oxigeno disponible: "))
oxigeno_requerido = int(input("ingrese la cantidad de oxigeno requerido: "))
provisiones_disponibles = int(input("ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("ingrese la cantidad de provisiones requeridas: "))

#Regla de decisión
#La misión podrá brindar soporte adecuado a la tripulación únicamente cuando el oxígeno disponible
#sea mayor o igual que el requerido y las provisiones disponibles sean mayores o iguales que las
#requeridas.
#• Si ambas condiciones se cumplen: “La nave posee recursos suficientes para la
#tripulación.”
#• En caso contrario: “La nave no posee recursos suficientes para la tripulación.”
#No se debe indicar todavía cuál recurso específico presenta el problema.

if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print ("la nave posee recursos suficientes para la tripulacion")
else:
    print ("la nave no posee los recursos suficientes para la tripulacion")