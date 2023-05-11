from math import sqrt # La función sqrt calcula la raíz cuadrada de un número.
print("Programa para la resolución a x*x + b x + c = 0")
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
if a != 0:
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print("El resultado de x1 es: {0:.3f} y el resultado de x2 es: {0:.3f}".format(x1, x2))

if a == 0:
    print("No es una ecuación de segundo grado.")