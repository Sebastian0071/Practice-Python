"""
Tu tarea: crea una función llamada presentarse que imprima tu nombre y 
tu ciudad. Llámala 3 veces.

Concepto clave: def nombre(): define. nombre() ejecuta. Sin paréntesis no pasa nada.
"""

def Presentarse():
    print("Seba")
    print("Santiago")

Presentarse()

"""
Tu tarea: crea describir_persona(nombre, edad) que 
imprima algo como: "Ana tiene 25 años". Pruébala con 3 personas distintas.
"""

def describir_persona(nombre):
    print(f"hola {nombre}")

describir_persona("Seba")

"""
Tu tarea: crea calcular_promedio(n1, n2, n3) que reciba 3 notas y devuelva el promedio
Luego imprime si el alumno aprobó (promedio >= 60).
"""

#<
def calcular_promedio(n1, n2, n3):

    promedio = (n1 + n2 + n3) / 3

    if promedio >= 60:
        print("Aprobado")
    elif promedio >= 50:
        print("Debes realizar examen")
    else:
        print("reprobado")


calcular_promedio(52, 52, 52)


"""
Tu tarea: crea calcular_descuento(precio, tipo_cliente). 
Si tipo_cliente es "vip" aplica 30% de descuento, 
si es "regular" aplica 10%, si es "nuevo" aplica 5%. Devuelve el precio final.
"""

def calcular_descuento(precio, tipo_cliente):

    if tipo_cliente == "vip":
        precio = precio - (precio * 0.30)
    elif tipo_cliente == "estandar":
        precio = precio - (precio * 0.10)
    else:
        precio

    print(f"tu precio es {precio}")


calcular_descuento(10000, "vip")