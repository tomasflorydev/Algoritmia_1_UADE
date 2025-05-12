# Ejercicio 1
""" fecha = input("Ingrese una fecha con el siguiente formato: DD MM AA")
tupla_fecha = (fecha.split())

n = int(input("Ingrese la cantidad de días que desea sumar a la fecha"))
lista_tupla = list(tupla_fecha)

dia = int(lista_tupla[0]) + n
lista_tupla[0] = dia

new_tupla_fecha = tuple(lista_tupla)
print(new_tupla_fecha) """

""" hora = int(input("Ingrese la hora"))
while hora > 23 or hora < 0:
    hora = int(input("Ingrese una hora valida"))
minutos = int(input("Ingrese los minutos"))
while minutos > 59 or minutos < 0:
    minutos = int(input("Ingrese una cantidad de minutos valida"))
tupla = (hora, minutos)
hora_n2 = int(input("Ingrese la hora"))
while hora_n2 > 23 or hora_n2 < 0:
    hora_n2 = int(input("Ingrese una hora valida"))
minutos_n2 = int(input("Ingrese los minutos"))
while minutos_n2 > 59 or minutos_n2 < 0:
    minutos_n2 = int(input("Ingrese una cantidad de minutos valida"))
tupla_n2 = (hora_n2, minutos_n2) """
"""
En esta primera parte se crean las tuplas y 
se hace la verificacion de valores
"""
""" minutos_totales = hora * 60 + minutos
minutos_totales_n2 = hora_n2 * 60 + minutos_n2

if minutos_totales > minutos_totales_n2:
    minutos_totales_n2 = minutos_totales_n2 + 1440 # Se suma 1440 ya que es la cantidad de minutos en un dia
    diferencia_minutos = minutos_totales_n2 - minutos_totales
    print(f"La diferencia es de {diferencia_minutos} minutos.")


elif minutos_totales_n2 > minutos_totales:
    minutos_totales = minutos_totales  + 1440
    diferencia_minutos = minutos_totales - minutos_totales_n2
    print(f"La diferencia es de {diferencia_minutos} minutos.")


else: 
    print("Ambos horarios corresponden al mismo momemnto")
 """

# Ejercico 2
""" nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def pedir_fecha():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    tupla = (dia, mes, año)  # Guardamos la tupla en una variable llamada 'tupla'
    return tupla

def fecha_en_texto(tupla):
    dia, mes, año = tupla  # Desempaquetamos la tupla en variables
    corte = 30  # Año de corte

    # Corregir el año si es de dos dígitos
    if año < 100:
        if año <= corte:
            año += 2000
        else:
            año += 1900

    # Armar y devolver el string con f-string
    fecha_texto = f"{dia} de {nombres_meses[mes - 1]} de {año}"
    print(fecha_texto)

fecha = pedir_fecha()  
fecha_en_texto(fecha)  
 """

#Ejercicio 3
""" def pedir_correo():
    correo = input("Ingrese su direccion de correo electronico")
    if "@" not in correo:
        tupla_correo = ()
        return tupla_correo
    else:
        usuario_dominio = correo.split("@")  
        dominio_extension = usuario_dominio[1].split(".")
        tupla_correo = (usuario_dominio[0], dominio_extension[0], dominio_extension[1])
        print(tupla_correo)


pedir_correo() """

#Ejercicio 5
""" import random
def generarFichas():
    #lado1 = random.randint(1,6)
    #lado2 = random.randint(1,6)
    lado1 = 1
    lado2 = 2
    
    ficha1 = (lado1,lado2)

    #lado4 = random.randint(1,6)
    #lado3 = random.randint(1,6)
    lado3 = 3
    lado4 = 4

    ficha2 = (lado3, lado4)

    return ficha1, ficha2

def conversion_tuplas_a_conjuntos(ficha1,ficha2):
    conjunto = set(ficha1)
    conjunto2 = set(ficha2)
    return conjunto, conjunto2

def verificar_encaje(conjunto, conjunto2):
    union_conjunto = conjunto | conjunto2
    if len(union_conjunto) < 4:
        print("Las fichas encastran")
    else:
        print("Las fichas no encastran") 

ficha1, ficha2= generarFichas()
conjunto, conjunto2 = conversion_tuplas_a_conjuntos(ficha1,ficha2)
verificar_encaje(conjunto, conjunto2)
print(ficha1,ficha2) """

#Ejercicio 6
""" import random
def generar_vectores():
    #ejeX_1 = random.randint(-10,10)
    #ejeY_1 = random.randint(-10,10)
    ejeX_1 = 2
    ejeY_1 = 3
    vector1 = (ejeX_1,ejeY_1)

    #ejeX_2 = random.randint(-10,10)
    #ejeY_2 = random.randint(-10,10)
    ejeX_2 = -3
    ejeY_2 = 2    
    vector2 = (ejeX_2, ejeY_2)

    return vector1,vector2

def verficar_ortogonales(vector1,vector2):
    if vector1[0] * vector2[0] + vector1[1] * vector2[1] == 0:
        print("Son ortogonales")
        return True
    else:
        print("No son ortogonales")
        return False

vector1, vector2 = generar_vectores()
verficar_ortogonales(vector1,vector2) """