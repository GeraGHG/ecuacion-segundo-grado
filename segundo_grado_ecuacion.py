print("Programa para la resolución a x*x + b x + c = 0")
a = 0
while a <= 0:
    a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

x1 = (-b + (pow(b, 2) * 4 * a * c) ** 2) / (2 * a)
x2 =(-b - (pow(b, 2) * 4 * a * c) ** 2) / (2 * a)
print("El resultado de x1 es: {0:.3f} y el resultado de x2 es: {1:.3f}".format(x1, x2))