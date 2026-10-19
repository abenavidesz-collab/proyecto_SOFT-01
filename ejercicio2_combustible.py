#Nombre del archivo (ejercicio2_combustible.py)
#Curso (SOFT-01)
#Nombres de los integrantes (Andres Benavides y Daniel Fezta)
#Fecha viernes 16 de octubre

#Descripción
#La agencia necesita verificar si una nave posee suficiente combustible antes de continuar con la
#preparación de la misión. Este ejercicio debe utilizar una estructura condicional simple.

#Datos solicitados
#Cantidad de combustible disponible.
#Cantidad de combustible requerida para llegar al destino.
#Cantidad de combustible requerida para regresar.

RESERVA_EMERGENCIA = 10
combustible_disponible = int(input("ingrese la cantidad de combustible disponible: "))
combustible_ida = int(input("ingrse la cantidad de combistible requerido para llegar al destino: "))
combustible_vuelta = int(input("ingrse la cantidad de combustible requerido para regresar: "))

#Cálculos requeridos
#Debe considerarse una reserva de emergencia de 10 unidades.
#Combustible total requerido = combustible de ida + combustible de regreso + 10
#Combustible adicional = combustible disponible - combustible total requerido

combustible_requerido = combustible_ida + combustible_vuelta + RESERVA_EMERGENCIA
combustible_adicional = combustible_disponible - combustible_requerido

#Regla de advertencia
#Si el combustible adicional es menor que 10 unidades, se debe mostrar únicamente en ese caso:
#“Advertencia: el margen adicional de combustible es bajo.”

if 10 > combustible_adicional:
    print (f""" 
    {"-" * 55}
    Advertencia: el margen adicional de combustible es bajo.
    {"-" * 55} """)

#Salidas obligatorias
#El programa debe mostrar siempre: combustible disponible, combustible requerido para llegar,
#combustible requerido para regresar, reserva de emergencia, combustible total requerido y
#combustible adicional disponible después de cubrir la misión.

print (f"""
{"-" * 15}
VERIFICACION DEL COMBUSTIBLE
{"-" * 15}
Combustible disponible: {combustible_disponible}
Combustible requerido para llegar: {combustible_ida}
Combustible requerido para regresar: {combustible_vuelta}
Reserva de emergencia: {RESERVA_EMERGENCIA}
{"-" * 15}
Combustible total requerido: {combustible_requerido}
Combustible adicional disponible después de cubrir la misión: {combustible_adicional}
{"-" * 15}""")