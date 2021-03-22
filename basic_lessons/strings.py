
str = "Hello World"

# upper() pone el string en mayuscula
print(str.upper())

# lower() pone el string en mayúscula
print(str.lower())

# Escribe la primera letra en mayúscula y el resto en minúscula
print(str.capitalize())

# replace("","") reemplaza los caracteres que introduzcamos
print(str.replace("Hello", "Bye"))

# count() cuenta el caracter introducido
print(str.count('l'))

# startswith() devuelve un booleano confirmando
# si un string comienza por lo intoducido
print(str.startswith("Hello"))

# endswith() devuelve un booleano confirmando
# si un string termina por lo intoducido
print(str.endswith("Planet"))

# split() separa los strings(con los ' ') y los transforma en listas

print(str.split())
# tambien puede separar por un caracter elegido:
print(str.split('o'))

# find() devuelve la posicion del caracter introducido
print(str.find('o'))

# len() devuelve la longitud de un string
print(len(str))
