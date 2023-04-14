# Dado un numero de 2 digitos, hallar un segundo numero con los digitos en orden inverso.
# Ejemplo: 35 -> 53

# OBTENEMOS NUMEROS
numero_original = int(input('Ingrese un numero: '))
numero_original_copia = numero_original
numero_reverso = 0

# INVERTIMOS NUMERO
while numero_original > 0:
    resto           = numero_original % 10
    numero_reverso  = numero_reverso  * 10 + resto
    numero_original = numero_original // 10
    
# Numero Original: 234
# 234 % 10   = 4  -> Resto: Con el modulo obtenemos el ultimo digito
# 0 * 10 + 4 = 4  -> Numero reverso
# 234 // 10  = 23 -> Numero original

# Numero Original: 23
# 23 % 10    = 3  -> Resto: Con el modulo obtenemos el ultimo digito
# 4 * 10 + 3 = 43 -> Numero reverso
# 23 // 10   = 2  -> Numero original

# Numero Original: 2
# 2 % 10      = 2   -> Resto: Con el modulo obtenemos el ultimo digito
# 43 * 10 + 2 = 432 -> Numero reverso
# 2 // 10     = 0   -> Numero original

# MOSTRAMOS NUMEROS
print(numero_original_copia)
print(numero_reverso)

