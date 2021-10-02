# -*- coding: utf-8 -*-

######################Ejercicio sobre funciones#############################
'''Ahora que ya conoce como se utilizan las funciones realice un programa que
haga lo mismo que el 2, es decir el de la obtención de áreas pero mediante
funciones, además verá como declarar una función principal para que al
momento que inicia el programa se vaya a ella y además usar la libreía math'''

import math
#Esta linea es para usar funciones de la librería math como las
#funciones trigonométricas


def areaTriangulo(base, altura):
    return (base * altura) / 2


def areaRectangulo(base, altura):
    return base * altura


def areaCirculo(radio):
    return math.pi * pow(radio, 2)


def MI_FUNCION():
    print "El área del triángulo es " + str(areaTriangulo(5, 6))
    print "El área del Rectangulo es " + str(areaRectangulo(5, 6))
    print "El área del Circulo es " + str(areaCirculo(15))

if __name__ == '__main__':
    MI_FUNCION()



















#base_t = 10
#altura_t = 27
#radio = 10
#base_r = 5
#altura_r = 29
#def main():
	#print "\t\t\tÁrea de figuras\n"
	#print "El área de un triángulo con base",base_t,"y altura",altura_t,"es de",area_t(base_t,altura_t),"\n"
	#print "El área de un círculo con radio",radio,"es de",area_c(radio),"\n"
	#print "El área de un rectángulo con base",base_r,"y altura",altura_r,"es de",area_r(base_r,altura_r),"\n"


#def area_t(base, altura):
    #return ( base * altura ) / 2


#def area_c(radio):
    #return math.pi * pow(radio,2)


#def area_r(base, altura):
    #return base * altura


#if __name__ == '__main__':
    #main()

