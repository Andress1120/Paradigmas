
"""
GRUPO D - Ejercicio 2

Instrucciones:
  a) Identifique el error y explique por qué el decorador usado es incorrecto.
     ¿Qué excepción se genera al ejecutar r.area()?
  b) Indique si el paradigma es Imperativo o Declarativo y justifique su respuesta.
"""

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    @staticmethod
    def area(self):                  # <- revisar esta línea
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


r = Rectangulo(4, 5)
print(f"Área: {r.area()}")
print(f"Perímetro: {r.perimetro()}")

"""
a) El error este en la linea 25 @staticmethod def area(self):, el motivo de la explicaciòn el decorador @staticmethod dice  que el método no recibe automáticamente la instancia (self) ni la clase (cls).
sin embargo, el método area está intentando usar self.base y self.altura, que pertenecen a la instancia del objeto.

Cuando llamado r.area() en python no pasa self automáticamente porque el método es estático, por lo que el parámetro self queda sin valor. 

b) El paradigma es Imperativo.

- El programa define pasos y procedimientos para calcular el área y el perímetro.
- Utiliza instrucciones, métodos y manipulación de estado del objeto (self.base, self.altura).
- Describe cómo realizar el cálculo, característica del paradigma imperativo dentro de la programación orientada a objetos.

"""
