# OPERACIONES ARITMETICAS
numero_1 = 10
numero_2 = 3

print(f"{numero_1 + numero_2}")
print(f"{numero_1 - numero_2}")
print(f"{numero_1 * numero_2}")
print(f"{numero_1 / numero_2}")
print(f"{numero_1 // numero_2}")
print(f"{numero_1 % numero_2}")
print(f"{numero_1 ** numero_2}")

# Operadores de Comparación
print(5 > 10)
print(5 >= 10)
print(5 < 10)
print(5 <= 10)
print(5 == 10)
print(5 != 10)

print("Ana" == "AnA")
print("Ana" != "AnA")
print("Ana" > "Ana")
print("AnaLu" > "AnaClau")
# print(ord("L"))
# print(ord("C"))
# print(ord("}"))
# print(len("AnaLu") > len("AnaClau"))

# OPERADORES LOGICOS
# NOT AND OR
# # NOT
num = 5
print(not (num < 10))

# AND
ingles = True
espanol = True

print("Ana" == "Jose" and 20 == 20 and "T" == "T")
print("Ana" == "Jose" or 20 == 20 or "T" == "T")

print(("Jose" == "Jose" or 90 == 20) and ("Pepito" == "Pepito" or -50 == 800))

# CREA UNA TABLA DE MULTIPLICAR DEL 1 al 5
# 1 * 1 = 1       2 * 1 = 2       3 * 1 = 3     4 * 1 = 4     5 * 1 = 5

salario = 516.1564

print(round(salario, 2))
print("{:.2f}".format(salario))
print(f"{salario:.2f}")
