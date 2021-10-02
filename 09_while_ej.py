# -*- coding: utf-8 -*-

###########################Ejercicio usando while##############################
import math
'''Ahora vamos a utilizar todo lo que sabe hasta ahora para hacer un menú que
nos permita elegir que programa queremos ejecutar, 1 si queremos el de la
obtención de áreas, 2 si queremos el de búsquedas, 3 si queremos el de
comparaciones y 4 si queremos salir, por el momento probarlo moviendo las
variables dentro del programa'''

def main():
	op = 3
	print """\t\t\t\tMenú\n1.-Cálculo de áreas\n2.-Búsquedas\n3.-Comparaciones\n4.-Salir\nEscoge la opción deseada:",op,"\n\n"""
	while op != 4:
		if op == 1:
			areas()
		else:
			if op == 2:
				busca_cadenas()
			else:
				if op == 3:
					comparaciones()
		op = 4

#############################Eligió  cálculo de áreas

def areas():
	base_t = 10
	altura_t = 27
	radio = 10
	base_r = 5
	altura_r = 29

	def area_t(base,altura):
		return ( base * altura ) / 2

	def area_c(radio):
		return math.pi * pow(radio,2)

	def area_r(base,altura):
		return base * altura

	print "\t\t\tÁrea de figuras\n"
	print "El área de un triángulo con base",base_t,"y altura",altura_t,"es de",area_t(base_t,altura_t),"\n"
	print "El área de un círculo con radio",radio,"es de",area_c(radio),"\n"
	print "El área de un rectángulo con base",base_r,"y altura",altura_r,"es de",area_r(base_r,altura_r),"\n"

###########################Eligió búsqueda de cadenas
def busca_cadenas():
	nombre = "Marco Antonio Martínez Quintana"

	print "\n\t\t\tBúsqueda de cadenas\n"
	print "La cadena completa comienza en la posición:",nombre.find("Marco Antonio Martínez Quintana")
	print "El nombre de pila cominza en la posición:",nombre.find("Marco Antonio")
	print "El apellido paterno en la posición:",nombre.find("Martínez")
	print "El apellido materno en la posición:",nombre.find("Quintana")
	print "Y las iniciales en la posición:",nombre.find("Marco"),nombre.find("Antonio"),nombre.find("Martínez"),"y",nombre.find("Quintana")
###########################Eligió comparaciones
def comparaciones():
	persona1 = 10
	persona2 = 30
	def verificam(p1,p2):
		return p1 < p2
	def verificaM(p1,p2):
		return p1 > p2
	print "\n\t\t\t\tComparaciones\n La edad de la persona 1 es de:",persona1,"años \n La edad de la persona 2 es de:",persona2,"años\n"
	print "La persona 1 es menor que la persona 2:",verificam(persona1,persona2)
	print "La persona 2 es menor que la persona 1:",verificam(persona2,persona1)
	print "La persona 1 es mayor que la persona 2:",verificaM(persona1,persona2)
	print "La persona 2 es mayor que la persona 1:",verificaM(persona2,persona1)

if __name__ == '__main__':
    main()
