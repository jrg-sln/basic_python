# -*- coding: utf-8 -*-

###############################Ejercicio de if#############################
'''Ahora que ya sabe usar el if y el else, hacer el mismo programa que el ejercicio anterior pero ahora si nos manda true escribir en consola verdadero y en caso contrario falso'''

persona1 = 10
persona2 = 30
true = "True"
def main():
	print "\n\t\t\t\tComparaciones\n La edad de la persona 1 es de:",persona1,"años \n La edad de la persona 2 es de:",persona2,"años\n"
	print "La persona 1 es menor que la persona 2:",traduce(str(verificam(persona1,persona2)))
	print "La persona 2 es menor que la persona 1:",traduce(str(verificam(persona2,persona1)))
	print "La persona 1 es mayor que la persona 2:",traduce(str(verificaM(persona1,persona2)))
	print "La persona 2 es mayor que la persona 1:",traduce(str(verificaM(persona2,persona1)))
def verificam(p1,p2):
	return p1 < p2
def verificaM(p1,p2):
	return p1 > p2
def traduce(palabra):
	if palabra == true:
		return "verdadero"
	else:
		return "falso"

if __name__ == '__main__':
	main()
