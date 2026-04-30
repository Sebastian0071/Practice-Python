# EL BUCLE WHILE
# ¿Para qué sirve?: Para iteración INDEFINIDA. Se repite mientras 
# la condición sea True. No sabes cuántas vueltas dará.
# Ejemplo: Mantener un menú abierto hasta que el usuario elija "Salir".

energia = 3
while energia > 0:
    # Sirve para procesos que dependen de un estado dinámico.
    print(f"Jugando... Energía restante: {energia}")
    energia -= 1 # Importante: modificar la condición para evitar bucles infinitos.