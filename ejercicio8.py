# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Andrés Benavides Zeledón, Daniel Festa
# Fecha: 15/11/2026
# Versión: 1.0
# Descripción: Evalúa si la nave puede regresar a la Tierra. Si puede,
#              simula el regreso día a día; si no, calcula cuántos días
#              sobrevive la tripulación varada y el recurso limitante.

# Constantes
# Consumo diario de cada recurso
CONSUMO_COMBUSTIBLE_DIA = 8
OXIGENO_TRIPULANTE_DIA = 2
ENERGIA_DIA = 5
PROVISIONES_TRIPULANTE_DIA = 1

# Formato de salida
ANCHO_SEPARADOR = 15

#Entrada de datos
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
duracion_viaje = int(input("Cantidad de días del viaje de ida: "))
combustible_disponible = int(input("Combustible disponible: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
energia_disponible = int(input("Energía disponible: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))

#Cálculos iniciales
# El regreso dura lo mismo que la ida. Ya no se exige la reserva.
combustible_regreso_requerido = duracion_viaje * CONSUMO_COMBUSTIBLE_DIA
consumo_oxigeno_dia = cantidad_tripulantes * OXIGENO_TRIPULANTE_DIA
consumo_provisiones_dia = cantidad_tripulantes * PROVISIONES_TRIPULANTE_DIA

#Decisión: ¿alcanza el combustible para regresar?
print()
if combustible_disponible >= combustible_regreso_requerido:
    #Caso A: simulación del regreso día a día
    dias_regreso = 0
    puede_continuar = True

    # Se usa while porque el regreso puede terminar antes por falta
    # de otro recurso (no se permite break).
    while dias_regreso < duracion_viaje and puede_continuar:
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
            dias_regreso = dias_regreso + 1
            print(f"Día {dias_regreso} | Combustible: {combustible_disponible} | "
                  f"Oxígeno: {oxigeno_disponible} | Energía: {energia_disponible} | "
                  f"Provisiones: {provisiones_disponibles}")
        else:
            # Cambiar la variable de control es lo que termina el ciclo.
            puede_continuar = False

    if puede_continuar:
        print(f"""La tripulación regresó exitosamente a la Tierra.
{"-" * ANCHO_SEPARADOR}
RECURSOS RESTANTES
{"-" * ANCHO_SEPARADOR}
Combustible: {combustible_disponible} unidades
Oxígeno: {oxigeno_disponible} unidades
Energía: {energia_disponible} unidades
Provisiones: {provisiones_disponibles} unidades
{"-" * ANCHO_SEPARADOR}""")
    else:
        print(f"El regreso se interrumpió en el día {dias_regreso + 1}.")
        # Condicionales independientes (no elif) para reportar TODOS
        # los recursos que no alcanzan.
        if combustible_disponible < CONSUMO_COMBUSTIBLE_DIA:
            print("Recurso insuficiente: combustible")
        if oxigeno_disponible < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")
        if energia_disponible < ENERGIA_DIA:
            print("Recurso insuficiente: energía")
        if provisiones_disponibles < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
else:
    #Caso B: la tripulación queda varada
    # División entera (//) porque solo cuentan los días completos.
    dias_oxigeno = oxigeno_disponible // consumo_oxigeno_dia
    dias_energia = energia_disponible // ENERGIA_DIA
    dias_provisiones = provisiones_disponibles // consumo_provisiones_dia

    # El mínimo se obtiene con condicionales (no se permite min()).
    dias_supervivencia = dias_oxigeno
    if dias_energia < dias_supervivencia:
        dias_supervivencia = dias_energia
    if dias_provisiones < dias_supervivencia:
        dias_supervivencia = dias_provisiones

    # Se revisan los tres recursos por separado para incluir los empates.
    # separador queda vacío para el primero y ", " para los siguientes.
    recursos_limitantes = ""
    separador = ""
    if dias_oxigeno == dias_supervivencia:
        recursos_limitantes = recursos_limitantes + separador + "oxigeno"
        separador = ", "
    if dias_energia == dias_supervivencia:
        recursos_limitantes = recursos_limitantes + separador + "energia"
        separador = ", "
    if dias_provisiones == dias_supervivencia:
        recursos_limitantes = recursos_limitantes + separador + "provisiones"
        separador = ", "

    print(f"""La tripulación quedó varada en el destino.
Días por oxígeno: {dias_oxigeno}
Días por energía: {dias_energia}
Días por provisiones: {dias_provisiones}
Supervivencia estimada: {dias_supervivencia} días
Recurso(s) limitante(s): {recursos_limitantes}""")