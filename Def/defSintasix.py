# LAS FUNCIONES (DEFINIDAS CON 'def')
# ¿Para qué sirven?: Son bloques de código que solo se ejecutan cuando se llaman.
# Su objetivo principal es la REUTILIZACIÓN (escribir una vez, usar mil)
# y la MODULARIDAD (dividir un problema grande en piezas pequeñas).

# 1. FUNCIÓN BÁSICA (Sin parámetros ni retorno)
# Sirve para agrupar pasos simples que se repiten sin variaciones.

def mostrar_bienvenida():
    # El cuerpo de la función está indentado.
    print("Iniciando el sistema...")
    print("Conexión establecida.")

# Llamada:
mostrar_bienvenida()


# 2. FUNCIÓN CON PARÁMETROS (Entrada de datos)
# ¿Para qué sirven?: Para que la función sea flexible y trabaje con
# diferentes valores cada vez que la invocas.

def calcular_impuesto(precio, tasa=0.19):
    # 'precio' es obligatorio.
    # 'tasa' tiene un valor por defecto (0.19), lo que lo hace opcional.
    total = precio * tasa
    print(f"El impuesto calculado es: {total}")

# Llamada:
calcular_impuesto(1000)        # Usa la tasa por defecto
calcular_impuesto(1000, 0.10)  # Sobrescribe la tasa


# 3. FUNCIÓN CON RETORNO (Salida de datos)
# ¿Para qué sirven?: Es la forma más profesional de usar funciones.
# En lugar de solo imprimir, la función "devuelve" un resultado al
# programa principal para que puedas seguir usándolo (guardarlo en variables, etc.).

def formatear_nombre(nombre, apellido):
    # Sirve para procesar datos y entregar un producto terminado.
    nombre_completo = f"{nombre.capitalize()} {apellido.capitalize()}"
    return nombre_completo 

# Guardamos el resultado en una variable para usarla después:
nombre_usuario = formatear_nombre("sebas", "developer")
print(f"Bienvenido, {nombre_usuario}")


# 4. TRATAMIENTO DE MÚLTIPLES ELEMENTOS (Listas y Diccionarios)
# ¿Para qué sirven?: Las funciones son ideales para procesar las 
# estructuras que vimos antes (listas/diccionarios) de forma automática.

def procesar_inventario(lista_productos):
    """
    Sirve para iterar sobre una lista y realizar lógica compleja.
    """
    for producto in lista_productos:
        if len(producto) > 5:
            print(f"Producto con nombre largo: {producto}")
        else:
            print(f"Producto corto: {producto}")

# Llamada pasando una lista:
mi_stock = ["Laptop", "Mouse", "Teclado"]
procesar_inventario(mi_stock)