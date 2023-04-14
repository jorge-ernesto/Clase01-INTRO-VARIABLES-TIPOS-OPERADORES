# Dado los lados de un rectangulo hallar:
# a. su perimetro
# b. su area
# c. su diagonal

import math

# OBTENEMOS DATOS PARA LOS CALCULOS
print("Lados de un rectangulo")
base   = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))

# CALCULAMOS PERIMETRO
perimetro = 2 * (base + altura)
print("El perimetro es:", perimetro)

# CALCULAMOS AREA
area = base * altura
print("El area es:", area)

# CALCULAMOS DIAGONAL
diagonal = ((base**2) + (altura**2)) ** 0.5
# diagonal = (base**2) + (altura**2)
# diagonal = math.sqrt(diagonal)
print("La diagonal es:", diagonal)
