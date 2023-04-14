# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos

# INGRESA CANTIDAD DE MINUTOS
can_min = int(input("Ingrese cantidad de minutos: "))

# CONVERTIMOS A HORAS Y MINUTOS
horas   = can_min // 60
minutos = can_min % 60

# MOSTRAMOS HORAS Y MINUTOS
print("Horas:" , horas, "Minutos:", minutos)