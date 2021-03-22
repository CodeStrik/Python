
# ESTRUCTURA IF ELSE:
# if (cond):
#     cuerpo de la condición
# else:
#     cuerpo del else

x = 3
if x != 3:
    print('x es distinto de 3')
else:
    print('x es igual a 3')

# Uso de elif:

color = 'azul'

if color == 'rojo':
    print('El color es rojo')
elif color == 'azul':
    print('El color es azul')
else:
    print('No es ni rojo ni azul')

# if anidado

nombre = "Juan"
apellido = 'Ramirez'

if nombre == 'Juan':
    if apellido == 'Ramirez':
        print("Eres Juan Ramirez")
    else:
        print("No eres Juan Ramirez")
