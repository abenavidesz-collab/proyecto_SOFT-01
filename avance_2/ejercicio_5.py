# Archivo: ejercicio5_destino.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Andrés Benavides Zeledón, Daniel Festa
# Fecha: 15/11/2026
# Versión: 1.0
# Descripción: Selecciona el destino de la misión, calcula los
#              recursos requeridos y decide si se autoriza el
#              lanzamiento.

#Constantes
# Nombres y duración del viaje de ida de cada destino
DESTINO_LUNA = "Luna"
DESTINO_MARTE = "Marte"
DESTINO_EUROPA = "Europa"

DIAS_LUNA = 3
DIAS_MARTE = 5
DIAS_EUROPA = 7

# Reglas de consumo del Avance 1
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10

OXIGENO_TRIPULANTE_DIA = 2
OXIGENO_EXTRA = 5

ENERGIA_DIA = 5
ENERGIA_EXTRA = 10

PROVISIONES_TRIPULANTE_DIA = 1
PROVISIONES_EXTRA = 3

# Mensajes y formato de salida
MENSAJE_DESTINO_INVALIDO = "Opción de destino no válida. La misión no puede planificarse."
ANCHO_SEPARADOR = 15

#Entrada de datos
nombre_mision = input("Nombre de la misión: ")
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
print(f"Destinos: 1. {DESTINO_LUNA}  2. {DESTINO_MARTE}  3. {DESTINO_EUROPA}")
# Se lee como texto: si el usuario escribe algo que no es número,
# cae en case _ en lugar de detener el programa.
opcion_destino = input("Opción de destino: ")

#Inicialización
# Se inicializan antes del match para que existan en todos los caminos;
# opcion_valida solo cambia a True si el destino existe.
opcion_valida = False
duracion_viaje = 0
nombre_destino = ""

#Decisión múltiple: destino
# Una sola variable con varios valores excluyentes -> match-case.
match opcion_destino:
    case "1":
        nombre_destino = DESTINO_LUNA
        duracion_viaje = DIAS_LUNA
        opcion_valida = True
    case "2":
        nombre_destino = DESTINO_MARTE
        duracion_viaje = DIAS_MARTE
        opcion_valida = True
    case "3":
        nombre_destino = DESTINO_EUROPA
        duracion_viaje = DIAS_EUROPA
        opcion_valida = True
    case _:
        print(MENSAJE_DESTINO_INVALIDO)

#Cálculos y autorización (solo si el destino es válido)
# Sin destino válido no hay días de viaje, así que no se debe calcular nada.
if opcion_valida:
    # Los recursos se piden solo cuando el destino existe: con una
    # opción inválida no se usarían para nada.
    combustible_disponible = int(input("Combustible disponible: "))
    oxigeno_disponible = int(input("Oxígeno disponible: "))
    energia_disponible = int(input("Energía disponible: "))
    provisiones_disponibles = int(input("Provisiones disponibles: "))

    combustible_ida = duracion_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_regreso = duracion_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = duracion_viaje * cantidad_tripulantes * OXIGENO_TRIPULANTE_DIA + OXIGENO_EXTRA
    energia_requerida = duracion_viaje * ENERGIA_DIA + ENERGIA_EXTRA
    provisiones_requeridas = duracion_viaje * cantidad_tripulantes * PROVISIONES_TRIPULANTE_DIA + PROVISIONES_EXTRA

    #Salida: resumen de la misión
    print(f"""
{"-" * ANCHO_SEPARADOR}
RESUMEN DE LA MISIÓN
{"-" * ANCHO_SEPARADOR}
Misión: {nombre_mision}
Destino: {nombre_destino}
Tripulantes: {cantidad_tripulantes}
Duración del viaje de ida: {duracion_viaje} días
{"-" * ANCHO_SEPARADOR}
Combustible para llegar: {combustible_ida} unidades
Combustible para regresar: {combustible_regreso} unidades
Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades
Combustible total requerido: {combustible_total} unidades
Oxígeno requerido: {oxigeno_requerido} unidades
Energía requerida: {energia_requerida} unidades
Provisiones requeridas: {provisiones_requeridas} unidades
{"-" * ANCHO_SEPARADOR}""")

    #Decisión anidada: autorización
    # El combustible se compara contra el TOTAL (ida + regreso + reserva)
    # porque la nave debe poder volver. Se usa >= porque tener exactamente
    # lo requerido sí alcanza.
    if (combustible_disponible >= combustible_total
            and oxigeno_disponible >= oxigeno_requerido
            and energia_disponible >= energia_requerida
            and provisiones_disponibles >= provisiones_requeridas):
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")