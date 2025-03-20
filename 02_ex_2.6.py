
# ex.1
# Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales.
print(type("Hola Mundo"), "str")	
print(type([1, 10, 100]), "list")	
print(type(-25), "int")	
print(type((8, 100, -12)), "tuple")	
print(type(1.167), "float")	
print(type(["Hola", "Mundo"]), "list")	
print(type(' '), "str")	
print(type((1, -5, "Hola!")), "tuple")
print(type({1,2,3,4,5}), "set")
print(type({}), "dict")
print(type({"nombre": "claudio"}), "dict")

# ex.2
# Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:
a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6)

print(a * 5)	# 50
print(a - b)	# 15
print(c + "Mundo")	# HolaMundo
print(c * 2)	# HolaHola
print(c[-1])	# a
print(c[1:])	# ola
print(d + d)	# [1, 2, 3, 1, 2, 3]
print(e[1])	    # 5
print(e+(6,7,8,9))    # (4, 5, 6, 6, 7, 8, 9)


#El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?
#     In [1]:
 
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3) / 3 # faltaban los parentesis
print("La nota media es", media) # 6

""" A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. 
Cada nota tiene un valor porcentual:
La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total """


nota1 = 1
nota2 = 6
nota3 = 10

def promedio(a, b, c):
    primera = a * 0.15
    segunda = b * 0.35
    tercera = c * 0.50
    resultado = (primera + segunda + tercera)
    print(resultado)

promedio(nota1, nota2, nota3)


# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
# Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

matriz = [
[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4]
]

for m in range(len(matriz)):
    matriz[m].append(sum(matriz[m]))
print("Matriz = ")
for linea in matriz:
    print(f"\t{linea}")

""" 
Consigna Sets
Crear un conjunto en Python que posea los siguientes elementos:
Países: Inglaterra, USA, México.
Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
Elimina a los países: Chile e Italia
Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?
Consigna Dicts
Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:
Ejemplo del output solicitado:
Juan tiene 25 años, y vive en Carrera 7 - Bogotá
 """

paises = {"Inglaterra", "USA", "México"}
mas_paises = {"Islandia", "Italia", "Argentina", "Portugal", "USA"}
total_paises = paises | mas_paises
print(total_paises)
total_paises.discard("Chile") #discard: si el elemento no está en el set, no da error
total_paises.remove("USA")
print(total_paises)

def info():
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese su edad: "))
    country = input("Ingrese en que pais vive: ")
    print(f"{name} tiene {age} años y vive en {country}")
info()


