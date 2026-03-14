"""
GRUPO D - Ejercicio 4

Instrucciones:
  a) Identifique el error, en qué línea ocurre y qué tipo de excepción genera.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

def contar_palabras(texto):
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo[palabra] + 1    # <- revisar esta línea
    return conteo


frase = "el gato y el perro y el pez"
resultado = contar_palabras(frase)
print(resultado)


"""
a) El error está en la línea 12, cuando una palabra aparece por primera vez, todavía no existe como clave en el diccionario conteo.
Entonces Python intenta acceder a conteo[palabra] antes de que exista.

b) Es un paradigma Imperativo: 

- El programa indica paso a paso cómo realizar la tarea.
- Utiliza estructuras de control como for y manipulación directa de un diccionario.
- Describe cómo se calcula el conteo, característica del paradigma imperativo.

"""