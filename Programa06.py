"""
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B.
"""

# OBTENEMOS INFORMACION DE PARTIDA DE CICLISTA
horas_a    = int(input('Hora de partida (HH): '))
minutos_a  = int(input('Minutos de partida (MM): '))
segundos_a = int(input('Segundos de partida (SS): '))
segundos_b = int(input('Tiempo de viaje (SS): '))
segundos   = segundos_b

# CALCULAMOS HORAS, MINUTOS Y SEGUNDOS DEL TIEMPO DE VIAJE
horas     = int(segundos / 60 / 60)
segundos -= horas*60*60
minutos   = int(segundos/60)
segundos -= minutos*60

# CALCULAMOS HORAS, MINUTOS Y SEGUNDOS DE LLEGADA
horas_a    += horas
minutos_a  += minutos
segundos_a += segundos

print("La hora de llegada es", horas_a)
print("Los minutos de llegada es", minutos_a)
print("Los segundos de llegada es", segundos_a)