# EL BUCLE FOR
# ¿Para qué sirve?: Para iteración DEFINIDA. Se usa cuando quieres 
# procesar elementos uno por uno de una colección o rango.
# Ejemplo: Aplicar un descuento a una lista de precios.

precios = [100, 200, 300]
for precio in precios:
    # Sirve para automatizar tareas repetitivas sobre un grupo de datos.
    print(f"Precio con IVA: {precio * 1.19}")