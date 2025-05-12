# Ejercicio 1
""" fecha = input("Ingrese una fecha con el siguiente formato: DD MM AA")
tupla_fecha = (fecha.split())

n = int(input("Ingrese la cantidad de días que desea sumar a la fecha"))
lista_tupla = list(tupla_fecha)

dia = int(lista_tupla[0]) + n
lista_tupla[0] = dia

new_tupla_fecha = tuple(lista_tupla)
print(new_tupla_fecha) """

horario = input("Ingrese una hora")

horario_tupla = (horario.split(":"))
lista_tupla = list(horario_tupla)

for i in lista_tupla:
    if lista_tupla[0] > 24:
        print("Error horario invalido")
        break
    
    elif lista_tupla[1] > 59:
        print("Error horario invalido")
        break
    else:
        print("Horario valido")