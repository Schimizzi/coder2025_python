
""" 
Realizar una función llamada año_bisiesto:
Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número, debe indicar que se ingrese un número.
"""


def es_numero(ano): # chequeo q sea un numero y de 4 digitos
    while True:
        if ano.isdigit() and len(str(ano)) == 4 and int(ano) >= 1000 and int(ano) <= 3000:
            break
        else:
            ano = input("ingrese un año: ")
    return int(ano)

def lista_bisiesto(): #creo una lista con los años bisiestos entre el 1000 y 3000
    lista_bi = list()
    for i in range(1000, 3001, 4):
        lista_bi.append(i)
    return lista_bi

def es_bisiesto(ano): # chequeo q el año q ingresó esté en la lista de bisiestos
    lista = lista_bisiesto()
    if ano in lista:
        print(f"[+] el {ano} es bisiesto")
    else:
        print(f"[+] el {ano} no es bisiesto")


year = input("Averigüe si es un año bisiesto, entre el 1000 y 3000: ")
ano = es_numero(year)    
es_bisiesto(ano)