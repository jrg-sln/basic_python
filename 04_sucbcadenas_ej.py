# -*- coding: utf-8 -*-

####################Ejercicio sobre el manejo de subcadenas###############


'''Ahora que ya sabe el uso de subcadenas, escriba un programa que muestre
su nombre completo,luego sólo su nombre de pila, después su apellido paterno,
luego apellido materno y por último sus iniciales juntas'''


Mi_nombre = 'Julio Cesar Saynez Fabian'

print "Nombre completo: " + Mi_nombre + "\n"
print "Nombre de pila " + Mi_nombre[:11]
print "Apellido paterno " + Mi_nombre[12:18]
print "Apellido materno " + Mi_nombre[19:]
print "Iniciales " + Mi_nombre[0] + Mi_nombre[6] + Mi_nombre[12] + Mi_nombre[19]
print ""

lista = Mi_nombre.split(' ')

print lista[0], lista[1]
print lista[2]
print lista[3]
print lista[0][0] + lista[1][0] + lista[2][0] + lista[3][0]







'''
nombre = "Marco Antonio Martínez Quintana"
print "\n\t\t\tManejo de subcadenas\n"
print "Nombre completo:",nombre[:]
print "Nombre de pila:",nombre[0:13]
print "Apellido paterno:",nombre[14:23]
print "Apellido materno:",nombre[24:]
print "Iniciales:",nombre[0]+nombre[6]+nombre[14]+nombre[24]
'''