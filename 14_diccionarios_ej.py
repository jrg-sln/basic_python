# -*- coding: utf-8 -*-

###########################Ejercicio sobre Diccionarios####################

'''Ahora que ya sabe usar diccionarios hacer un programa que maneje el precio
 y nombre de un inventario en una tienda de abarrotes'''
inventario = {}

def actualiza(c, a, m):
    inventario[c][a] = m


def main():
    #Inicializando diccionario
    inventario['refresco'] = {'precio': '$15', 'cantidad': '100'}
    inventario['papas'] = {'precio': '$5', 'cantidad': '30'}
    inventario['leche'] = {'precio': '$10', 'cantidad': '25'}
    inventario['frijol'] = {'precio': '$12', 'cantidad': '50'}
    inventario['dulces'] = {'precio': '$2', 'cantidad': '45'}
    print ("El inventario actual es:\n")
    for i in inventario:
        print (i, inventario[i])
    r = "refresco"
    p = "precio"
    c = "cantidad"
    d = "dulces"
    precior = "16"
    cantidadd = "39"
    actualiza(r, p, precior)
    actualiza(d, c, cantidadd)
    inventario['leche']['precio'] = '15'
    print ("\nEl inventario después de las modificaciones es:\n")
    for i in inventario:
        print (i, inventario[i])


if __name__ == '__main__':
    main()
