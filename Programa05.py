"""
Un vendedor recibe un sueldo base mas un 10% extra por comision de sus ventas. 
El vendedor desea saber:
    - Cuanto dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes 
    - El total que recibira en el mes tomando en cuenta su sueldo base y comisiones
"""

# OBTENEMOS SUELDO Y MONTOS DE LAS VENTAS
sueldo = int(input('Ingrese el sueldo: '))
venta1 = int(input('Ingrese el monto generado por la primera venta: '))
venta2 = int(input('Ingrese el monto generado por la segunda venta: '))
venta3 = int(input('Ingrese el monto generado por la tercera venta: '))

# CALCULAMOS COMISION
comision1      = venta1*0.1
comision2      = venta2*0.1 
comision3      = venta3*0.1
comision_total = comision1+comision2+comision3
importe_total  = sueldo+comision_total

# MOSTRAMOS COMISION Y TOTAL SUELDO
print("La comision por las 3 ventas es:", comision_total)
print("El importe total del mes es:", importe_total)
