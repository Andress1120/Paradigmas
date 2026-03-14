
README – Parcial Grupo D

Ejercicio 1 – Fibonacci

Error:
Se usa fibonacci(n - 3) en vez de fibonacci(n - 2), lo que da resultados incorrectos.

Corrección:

return fibonacci(n - 1) + fibonacci(n - 2)

Paradigma: Imperativo, porque el programa indica paso a paso cómo calcular el resultado.

Ejercicio 2 – Rectángulo

Error:
Se usa @staticmethod en el método area, pero el método usa self.

Excepción:
TypeError: area() missing 1 required positional argument: 'self'

Corrección:
Quitar @staticmethod.

Paradigma: Imperativo (Programación Orientada a Objetos).

Ejercicio 3 – Temperaturas

Error:
Se usa map antes de filter, convirtiendo los valores en booleanos.

Corrección:

resultado = list(map(lambda x: x * 1.5, filter(lambda x: x > 30, temperaturas)))

Paradigma: Declarativo, porque usa map y filter para transformar datos.

Ejercicio 4 – Contar palabras

Error:
Se intenta aumentar una clave que no existe en el diccionario.

Excepción:
KeyError

Corrección:

if palabra in conteo:
    conteo[palabra] += 1
else:
    conteo[palabra] = 1

Paradigma: Imperativo, porque usa instrucciones paso a paso (for, if).