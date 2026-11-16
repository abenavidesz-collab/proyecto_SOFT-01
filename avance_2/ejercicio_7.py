# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Andrés Benavides Zeledón, Daniel Festa
# Fecha: 15/11/2026
# Versión: 1.0
# Descripción: Presenta un menú repetitivo de actividades de
#              exploración en el destino, descuenta los recursos
#              y acumula los puntos científicos obtenidos.

# Constantes
# Nombre, costo y puntos de cada actividad
ACTIVIDAD_ANALIZAR = "Analizar terreno"
ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

ACTIVIDAD_MUESTRA = "Recolectar muestra"
ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20

ACTIVIDAD_OBSERVACION = "Realizar observación"
ENERGIA_OBSERVACION = 5
PROVISIONES_OBSERVACION = 0
PUNTOS_OBSERVACION = 8

# Mensajes y formato de salida
MENSAJE_OPCION_INVALIDA = "Opción no válida."
MENSAJE_RECURSOS_INSUFICIENTES = "Recursos insuficientes para realizar la actividad. La exploración finaliza."
ANCHO_SEPARADOR = 15

#Entrada de datos
energia_disponible = int(input("Energía disponible: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))

#Inicialización
# Contadores y acumulador empiezan en 0; el menú se repite
# mientras continuar_exploracion sea True.
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
continuar_exploracion = True

#Ciclo del menú: cada iteración es una elección del usuario
# Se usa while porque no se sabe cuántas veces se repetirá el menú.
while continuar_exploracion:
    print(f"""
{"-" * ANCHO_SEPARADOR}
1. {ACTIVIDAD_ANALIZAR}
2. {ACTIVIDAD_MUESTRA}
3. {ACTIVIDAD_OBSERVACION}
4. Finalizar exploración
{"-" * ANCHO_SEPARADOR}""")
    opcion_actividad = input("Seleccione una actividad: ")

    # Se reinician en cada vuelta para que no arrastren
    # el valor de la actividad anterior.
    actividad_valida = False
    es_recoleccion = False

    #Decisión múltiple: actividad elegida
    match opcion_actividad:
        case "1":
            nombre_actividad = ACTIVIDAD_ANALIZAR
            costo_energia = ENERGIA_ANALIZAR
            costo_provisiones = PROVISIONES_ANALIZAR
            puntos_actividad = PUNTOS_ANALIZAR
            actividad_valida = True
        case "2":
            nombre_actividad = ACTIVIDAD_MUESTRA
            costo_energia = ENERGIA_MUESTRA
            costo_provisiones = PROVISIONES_MUESTRA
            puntos_actividad = PUNTOS_MUESTRA
            actividad_valida = True
            es_recoleccion = True
        case "3":
            nombre_actividad = ACTIVIDAD_OBSERVACION
            costo_energia = ENERGIA_OBSERVACION
            costo_provisiones = PROVISIONES_OBSERVACION
            puntos_actividad = PUNTOS_OBSERVACION
            actividad_valida = True
        case "4":
            # Cambiar la variable de control es lo que termina el ciclo.
            continuar_exploracion = False
        case _:
            # El estado no cambia y el menú se vuelve a mostrar.
            print(MENSAJE_OPCION_INVALIDA)

    #Decisión anidada: ¿alcanzan los recursos para la actividad?
    if actividad_valida:
        # Se verifica ANTES de descontar: si no alcanza, nada se modifica.
        if energia_disponible >= costo_energia and provisiones_disponibles >= costo_provisiones:
            energia_disponible = energia_disponible - costo_energia
            provisiones_disponibles = provisiones_disponibles - costo_provisiones
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad
            # Solo recolectar muestra aumenta el contador de muestras.
            if es_recoleccion:
                muestras_recolectadas = muestras_recolectadas + 1
            print(f"Actividad realizada: {nombre_actividad}. Puntos obtenidos: {puntos_actividad}")
        else:
            print(MENSAJE_RECURSOS_INSUFICIENTES)
            continuar_exploracion = False

#Salida: resumen de la exploración
print(f"""
{"-" * ANCHO_SEPARADOR}
RESUMEN DE LA EXPLORACIÓN
{"-" * ANCHO_SEPARADOR}
Actividades realizadas: {actividades_realizadas}
Muestras recolectadas: {muestras_recolectadas}
Puntos científicos: {puntos_cientificos}
Energía restante: {energia_disponible} unidades
Provisiones restantes: {provisiones_disponibles} unidades
{"-" * ANCHO_SEPARADOR}""")