#Nombre del archivo (ejercicio1_recursos.py)
#Curso (SOFT-01)
#Nombres de los integrantes (Andres Benavides y Daniel Fezta)
#Fecha viernes 16 de octubre

#Ejercicio 1: Calculo de recursos necesarios para una mision
#Descripcion
#Antes de autorizar una mision, la agencia necesita determinar aproximadamente cuantos recursos
#seran necesarios para realizar el viaje. 
#Este ejercicio debe resolverse principalmente mediante flujo secuencial.

#Reserva: toda mision debe transportar 10 unidades adicionales de combustible para
#emergencias.

CONSUMO_COMBUSTIBLE_IDA = 8
CONSUMO_COMBUSTIBLE_REGRESO = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_DIA = 2
OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3

#Datos solicitados:
#Nombre de la mision.
#Cantidad de tripulantes.
#Cantidad de dias estimados para llegar al destino.

nombre_mision = input("Ingrese el nombre de la misión: ")
cant_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de dias estimados para el viaje: "))

#Calculos requeridos
#Combustible de ida: por cada dia de viaje se consumen 8 unidades de combustible.

combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_IDA

#Combustible de regreso: el viaje de regreso tiene la misma duracion que el de ida y consume tambien 8 unidades
#por dia.

combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_REGRESO

#Combustible total teniendo en cuenta todos los datos

combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

#Oxigeno: cada tripulante consume 2 unidades por dia (solo viaje de ida) mas 5 unidades de
#emergencia.

oxigeno_requerido = cant_tripulantes * dias_viaje * CONSUMO_OXIGENO_DIA + OXIGENO_EMERGENCIA

#Energia: la nave consume 5 unidades por dia de ida mas 10 unidades para las
#operaciones de exploracion.

energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIA + ENERGIA_EXPLORACION

#Provisiones: cada tripulante consume 1 unidad por dia de ida mas 3
#unidades adicionales.

provisiones_requeridas = dias_viaje * cant_tripulantes + PROVISIONES_ADICIONALES

#Salida esperada (ejemplo)
#Mision: Explorador I
#Tripulantes: 3
#Duracion estimada hasta el destino: 5 dias
#Combustible para llegar: 40 unidades
#Combustible para regresar: 40 unidades
#Reserva de combustible: 10 unidades
#Combustible total requerido: 90 unidades
#Oxigeno requerido: 35 unidades
#Energia requerida: 35 unidades
#Provisiones requeridas: 18 unidades

print (f"""
{"-" * 15}
RECURSOS PARA LA MISION:
{"-" * 15}
Misión: {nombre_mision}
Tripulantes: {cant_tripulantes}
Duración estimada hasta el destino: {dias_viaje} dias
{"-" * 15}
Combustible para llegar: {combustible_ida} unidades
Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades
Combustible total requerido: {combustible_total} unidades
Oxígeno requerido: {oxigeno_requerido} unidades
Energía requerida: {energia_requerida} unidades
Provisiones requeridas: {provisiones_requeridas} unidades
{"-" * 15}""")