
#################################################################################################################################################
# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura

def area_rectangulo(b,a):
    area = b * a
    return f"El area del rectangulo ingresado es de {area}"

print(area_rectangulo(10, 15))


#################################################################################################################################################
# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

def area_circulo(r):
    area = 3.14 * r**2
    return f"El area del circulo ingresado es de {area}"

print(area_circulo(5))


#################################################################################################################################################
# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5' """

def relacion(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    elif a < b:
        return -1
    else:
        print("fruta")

print(relacion(5, 10)) # -1
print(relacion(10, 5)) #  1
print(relacion(5, 5))  #  0


#################################################################################################################################################
# Realiza una función llamada promedio() que, a partir de dos números, devuelva su promedio

def promedio(*args):
    suma = sum(args)
    prom = suma / len(args)
    print(f"[+] el promedio de las notas ingresadas es {prom}")

promedio(10, 20, 30) # el promedio es 20


#################################################################################################################################################
# Realiza una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:
#   Devolver el límite inferior si el número es menor que éste
#   Devolver el límite superior si el número es mayor que éste.
#   Devolver el número sin cambios si no se supera ningún límite.
#   Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(a, b, c):
    # a => numero a recortar
    # b => limite inferior
    # c => limite superior

    if a >= b and a <= c:
        return a
    elif a <= b:
        return b
    elif a >= c:
        return c
    else:
        return "furta"
    
print(recortar(-2, 0, 10))  # limite a 0
print(recortar(4, 0, 10))   # 4 sin recorte
print(recortar(22, 0, 10))  # limite a 10

#################################################################################################################################################




