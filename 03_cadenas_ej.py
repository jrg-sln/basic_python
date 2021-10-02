# -*- coding: utf-8 -*-

###################Ejercicio sobre el uso de cadenas#####################

'''Ahora que ya sabe manejar cadenas tome su ejemplo anterior y agreguele
formato, es decir título, área de la figura y su valor delante, ademas      ponga el número del programa utilizando la función str'''

num_programa = 3
print "\nPrograma número " + str(num_programa) + "\n"
print "\t\t\tCálculo del Área de Figuras\n" #Título

#Area del triángulo
base_t = 10
altura_t = 27
area_t = (base_t * altura_t) / 2
print "El área de un triángulo con base",base_t,"y altura",altura_t,"es de",area_t,"\n"
#Area del círculo
Pi = 3.1416
radio = 10
area_c = Pi * ((radio) ^ 2)
print "El área de un círculo con radio",radio,"es de",area_c,"\n"
#Area del rectángulo
base_r = 5
altura_r = 29
area_r = base_r * altura_r
print "El área de un rectángulo con base",base_r,"y altura",altura_r,"es de",area_r,"\n"
