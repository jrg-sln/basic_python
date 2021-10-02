# -*- coding: utf-8 -*-

##############Ejercicio sobre funciones con listas#######################

'''Ahora que ya sabe manejar las funciones de las listas hacer un programa
que simule el registro de alumnos en una lista y al final la imprima en
 forma descendente'''


def alta(c, a):
    c.append(a)
    return c


def baja(c, b):
    del[c[b]]
    return c


def main():
    alumnos = ["Marco", "Ricardo", "Gladys"]
    print "\t\t\t\tBase de datos\nLa base actual es la suiguiente:\n", alumnos
    a = "Pepe"
    alumnos = alta(alumnos, a)
    alumnos = baja(alumnos, alumnos.index('Marco'))
    print "\nAhora la base es: "
    for i in alumnos:
        print i
if __name__ == '__main__':
    main()
