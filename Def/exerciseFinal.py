"""
Tu tarea: crea un sistema con 3 funciones: validar_nota(nota) que devuelva True/False
si está entre 0-100, letra_nota(nota) que devuelva 
A/B/C/D/F, 
y reporte_alumno(nombre, nota) que use las dos anteriores e imprima un reporte completo.
"""

def validar_nota(nota):
    
    if nota < 0 and nota > 100:
        nota = False
    elif nota > 0 and nota < 100:
        nota = True
    
    return nota

def letra_nota(nota):

    if nota >= 90:
        print("A")
    elif nota >= 80:
        print("B")
    elif nota >= 70:
        print("C")
    elif nota >= 60:
        print("D")
    else:
        print("F")

    
    

def reporte_alumno(nombre, nota):
    print(f"el reporte es: {nombre} nota: {nota}")

validar_nota(100)
letra_nota(100)
reporte_alumno("seba", 100)
