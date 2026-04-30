# EL CONDICIONAL IF/ELIF/ELSE
# ¿Para qué sirve?: Para la toma de decisiones. El programa evalúa 
# una condición booleana (True/False) y decide qué camino tomar.
# Ejemplo: Control de acceso o validación de datos.

edad = 20
if edad >= 18:
    # Se usa para ejecutar código solo si la condición es verdadera.
    print("Acceso concedido.")
elif edad > 0:
    # Se usa para añadir múltiples caminos alternativos.
    print("Acceso denegado: eres menor.")
else:
    # Se usa como red de seguridad si ninguna condición anterior se cumplió.
    print("Error: Edad no válida.")