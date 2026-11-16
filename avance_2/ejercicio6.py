# Archivo: ejercicio6_viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Andrés Benavides Zeledón, Daniel Festa
# Fecha: 15/11/2026
# Versión: 1.0
# Descripción: Simula día a día el viaje hacia el destino,
#              descontando los recursos y deteniéndose si alguno
#              no alcanza para completar el día.

# Constantes
# Consumo diario de cada recurso
CONSUMO_COMBUSTIBLE_DIA = 8
OXIGENO_TRIPULANTE_DIA = 2
ENERGIA_DIA = 5
PROVISIONES_TRIPULANTE_DIA = 1

# Formato de salida
ANCHO_SEPARADOR = 15

#Entrada de datos
duracion_viaje = int(input("Cantidad de días del viaje: "))
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
combustible_disponible = int(input("Combustible disponible: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
energia_disponible = int(input("Energía disponible: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))

#Inicialización
# El oxígeno y las provisiones dependen de la tripulación, así que su
# consumo diario se calcula una sola vez antes del ciclo.
consumo_oxigeno_dia = cantidad_tripulantes * OXIGENO_TRIPULANTE_DIA
consumo_provisiones_dia = cantidad_tripulantes * PROVISIONES_TRIPULANTE_DIA
dias_transcurridos = 0
puede_continuar = True

#Ciclo: cada iteración es un día de viaje
# Se usa while porque el ciclo termina por dos motivos: completar los
# días o quedarse sin recursos (no se permite break).
print()
while dias_transcurridos < duracion_viaje and puede_continuar:
    # Se verifica ANTES de consumir: si un recurso no alcanza,
    # el día no se realiza y no se descuenta nada.
    if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA
            and oxigeno_disponible >= consumo_oxigeno_dia
            and energia_disponible >= ENERGIA_DIA
            and provisiones_disponibles >= consumo_provisiones_dia):
        combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno_disponible = oxigeno_disponible - consumo_oxigeno_dia
        energia_disponible = energia_disponible - ENERGIA_DIA
        provisiones_disponibles = provisiones_disponibles - consumo_provisiones_dia
        dias_transcurridos = dias_transcurridos + 1
        print(f"Día {dias_transcurridos} | Combustible: {combustible_disponible} | "
              f"Oxígeno: {oxigeno_disponible} | Energía: {energia_disponible} | "
              f"Provisiones: {provisiones_disponibles}")
    else:
        # Cambiar la variable de control es lo que termina el ciclo.
        puede_continuar = False

#Salida de resultados
if puede_continuar:
    print(f"""La nave llegó al destino en {dias_transcurridos} días.
{"-" * ANCHO_SEPARADOR}
RECURSOS RESTANTES
{"-" * ANCHO_SEPARADOR}
Combustible: {combustible_disponible} unidades
Oxígeno: {oxigeno_disponible} unidades
Energía: {energia_disponible} unidades
Provisiones: {provisiones_disponibles} unidades
{"-" * ANCHO_SEPARADOR}""")
else:
    # El día fallido es el siguiente al último completado.
    print(f"Viaje interrumpido en el día {dias_transcurridos + 1}.")
    # Condicionales independientes (no elif) para reportar TODOS
    # los recursos que no alcanzan, no solo el primero.
    if combustible_disponible < CONSUMO_COMBUSTIBLE_DIA:
        print("Recurso insuficiente: combustible")
    if oxigeno_disponible < consumo_oxigeno_dia:
        print("Recurso insuficiente: oxígeno")
    if energia_disponible < ENERGIA_DIA:
        print("Recurso insuficiente: energía")
    if provisiones_disponibles < consumo_provisiones_dia:
        print("Recurso insuficiente: provisiones")
    print(f"Días completados: {dias_transcurridos}")