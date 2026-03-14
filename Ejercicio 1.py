
"""
GRUPO D - Ejercicio 1

Instrucciones:
  a) El código no produce error de sintaxis pero el resultado es incorrecto.
     Identifique el error lógico e indique en qué línea se encuentra.
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 3)  # <- revisar esta línea


for i in range(6):
    print(f"fibonacci({i}) = {fibonacci(i)}")


"""
a) El error es que para calcular correctamente la serie de Fibonacci, cada término debe ser la suma de los dos anteriores, Pero el código usa n - 3, lo cual rompe la definición de la serie.
Correciòn del codigo es -> return fibonacci(n - 1) + fibonacci(n - 2)

El error esta en la linea 15.

b) El paradigma utilizado es Imperativo:

-El programa describe paso a paso cómo calcular el resultado.
-Usa instrucciones explícitas, control de flujo (if) y ejecución secuencial.
-Indica cómo debe realizarse el cálculo, no solo qué resultado se desea.

"""