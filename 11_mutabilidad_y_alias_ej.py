# -*- coding: utf-8 -*-

######################Ejercicio sobre mutabilidad y alias#####################
'''Ahora que ya conoce como se maneja la mutabilidad y las referencias, hacer
un ejercicio en el que se tenga una lista para actualizar datos de un usuario,
 admás implementelo con  una función para actualizar'''


def actualizae(l, n):
    lista = l
    lista[1] = n


def main():
    print "\t\t\tRegistro de usuarios"
    datos = ["Marco", 20]
    print "Los datos son:", datos[0], datos[1]
    dato_nuevo = 21
    actualizae(datos, dato_nuevo)
    print "Los datos son:", datos[0], datos[1]
if __name__ == '__main__':
    main()
