# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura



def base():
    while True:        
        b = input("ingrese la base del rectangulo: ")
        if b.isdigit():
            return int(b)        
        else: print("ingrese un digito valido")
base = base()

def altura():
    while True:
        h = input("ingrese la altura del rectangulo:")
        if h.isdigit():
            return int(h)
        else: print("ingrese un digito valido!")
altura = altura()

def area_rect(b, h):
    area = base * altura
    print(f"el area de un rectangulo de base {base} y altura {altura} es de {area}")


area_rect(base, altura)