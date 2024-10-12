# Strings
saludo = "Hola Mundo"
salud = 209


# Flexibilidad
# var = "Estudiantes "CE""
var = 'Estudiantes "CE"'
print(var)

# Secuencias de Escape
var = "Estudiantes \"CE\""
print(var)
var = "Bienvenidos a su \ncurso de \nPython"
print(var)
var = "\\nHola"
print(var)

# INDEXACION
nombre = "Pepito Quiere a Pepita"
print(nombre[7])
print(nombre[-8])

# # SLACING
print(nombre[0:6])
print(nombre[-6:-2])
print(nombre[-8:])

# STRIDE
print(nombre[::3])
print(nombre[7:13:2])

# String Son Inmutables
nombre = "Antonio Ramirez"
nombre[:7] = "Joseantonio"
print(nombre[0:7])

# Formateando Cadenas
# Sin variables
nombre = "Antonio"
apellido = "Ramirez"
print("Saludos:", nombre, apellido)
print("Hola Mundo")

# Funcion Formato
nombre = "Antonio2"
apellido = "Ramirez2"
print("Saludos2: {} {}".format(nombre, apellido))
print("Hola Mundo 2".format())

# F string, Cadenas Literales
nombre = "Antonio3"
apellido = "Ramirez3"
print(f"Saludos3: {nombre} {apellido}")
print(f"Hola Mundo 3")


# Separador
var = "Antonio"
var_2 = "Jose"
anio = 2024
print("Hola", var, "\nHola", var_2, "\nAño:", anio)

# COncatenación
var = "Antonio"
var_2 = "Jose"
anio = 2024
print("Hola " + var + "\nHola " + var_2 + "\nAño " + str(anio))

# Métodos de Strings
saludo_1 = "Bienvenidos estudiantes CE"
saludo_2 = "        Hola amigos       "

print(saludo_1.upper())
print(saludo_1.lower())
print(saludo_1.capitalize())
print(saludo_1.title())
print(saludo_2.strip())
print(saludo_2.lstrip())
print(saludo_2.rstrip())

print(saludo_2.strip().title())


"""NUMEROS INTEGERS"""
numero = 20
edad = 20
salario = -1564
print(type(numero))

numero = "50"
numero_casting = int(numero)
print(numero_casting)

venta_final = 156_498_189_189_198
print(venta_final)

"""Floating | Float"""
numero = -50.60
print(type(numero))

"""Booleanos | Bools"""
casado = True
print(type(casado))
