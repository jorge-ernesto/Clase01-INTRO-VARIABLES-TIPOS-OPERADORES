# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
# Recordar que la formula para la conversion es
# C = (F-32)*5/9

# OBTENEMOS GRADOS FAHRENHEIT
fahrenheit = int(input("Ingrese grados Fahrenheit: "))

# CONVERTIMOS A CELSIUS
celsius = (fahrenheit-32)*5/9
print("Los grados Celsius son: ", celsius)
