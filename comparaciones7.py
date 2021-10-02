# -*- coding: utf-8 -*-

###########################Ejercicio sobre comparaciones####################
'''Ahora que ya sabe utilizar comparaciones hacer un programa que contenga la edad de varias personas y decir si es cierta o falsa la afirmación mediante una función, además use la impementación de la función main'''

persona1 = 10
persona2 = 30

def main():
	print "\n\t\t\t\tComparaciones\n La edad de la persona 1 es de:",persona1,"años \n La edad de la persona 2 es de:",persona2,"años\n"
	print "La persona 1 es menor que la persona 2:" + str(verificam(persona1,persona2))
	print "La persona 2 es menor que la persona 1:",verificam(persona2,persona1)
	print "La persona 1 es mayor que la persona 2:",verificaM(persona1,persona2)
	print "La persona 2 es mayor que la persona 1:",verificaM(persona2,persona1)
def verificam(p1,p2):
	return p1 < p2
def verificaM(p1,p2):
	return p1 > p2
if __name__ == '__main__':
    main()
