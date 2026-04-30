# LISTAS (MUTABLES Y ORDENADAS)
# ¿Para qué sirven?: Son el contenedor estándar para colecciones de 
# objetos del mismo tipo o relacionados que van a cambiar con el tiempo.
# Ejemplo: Lista de usuarios conectados, historial de mensajes.

tareas = ["Estudiar", "Programar"] 
tareas.append("Descansar") # Sirve para añadir elementos dinámicamente.
tareas[0] = "Repasar Python" # Sirve para actualizar datos existentes.


# TUPLAS (INMUTABLES Y ORDENADAS)
# ¿Para qué sirven?: Para agrupar datos que NO deben cambiar. 
# Son más ligeras y rápidas que las listas y protegen la integridad.
# Ejemplo: Configuración de colores (RGB), dimensiones, coordenadas.

configuracion_db = ("127.0.0.1", 5432, "admin")

# Al ser inmutable, el programa garantiza que el puerto (5432) 
# no será modificado accidentalmente durante la ejecución.


# DICCIONARIOS (MAPAS DE CLAVE-VALOR)
# ¿Para qué sirven?: Para asociar etiquetas (claves) con datos (valores). 
# Es la forma más rápida de buscar un dato sin recorrer toda la estructura.
# Ejemplo: Un registro de base de datos o un objeto JSON de una API.

empleado = {
    "id": 1024,
    "nombre": "Sebas",
    "puesto": "Software Developer"
}
# Sirve para acceder a la información de forma descriptiva:
print(f"El empleado es: {empleado['nombre']}")