"""
GRUPO D - Ejercicio 3

Instrucciones:
  a) El código no genera error de sintaxis pero produce un resultado incorrecto.
     Identifique el error lógico y explique cómo corregirlo.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

temperaturas = [22, 35, 18, 40, 28, 15, 37]

# Objetivo: obtener las temperaturas mayores a 30, aumentadas en un 50%
resultado = list(filter(
    lambda x: x * 1.5,
    map(lambda x: x > 30, temperaturas)
))

print(f"Temperaturas ajustadas: {resultado}")

"""
a) El error está en el orden y uso de map y filter.

Explicaciòn y como correguirlo

Primero filtrar, luego transformar, De esta forma:
- filter selecciona 35, 40, 37
- map aplica el aumento del 50%

b) En Paradigma Declarativo porque se utilizan funciones como map y filter para indicar qué transformación se quiere aplicar a los datos, sin describir paso a paso cómo recorrer la lista.

"""