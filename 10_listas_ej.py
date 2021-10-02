# -*- coding: utf-8 -*-

#############################Ejercicio de listas##############################3
'''Ahora que ya sabe usar listas vamos a hacer una tabla de las tablas de multiplicar, es decir si pedimos 6 x 8 lo busque en una lista anidada y nos arroje el resultado'''



tn = [range(1,11,1),
    range(2,21,2),
    range(3,31,3),
    range(4,41,4),
    range(5,51,5),
    range(6,61,6),
    range(7,71,7),
    range(8,81,8),
    range(9,91,9),
    range(10,101,10)
    ]

print tn

tabla=[[1,2,3,4,5,6,7,8,9,10],
    [2,4,6,8,10,12,14,16,18,20],
    [3,6,9,12,15,18,21,24,27,30],
    [4,8,12,16,20,24,28,32,36,40],
    [5,10,15,20,25,30,35,40,45,50],
    [6,12,18,24,30,36,42,48,54,60],
    [7,14,21,28,35,42,49,56,63,70],
    [8,16,24,32,40,48,56,64,72,80],
    [9,18,27,36,45,54,63,72,81,90],
    [10,20,30,40,50,60,70,80,90,100]]

def calcula(n1,n2):
	return tn[n1-1][n2-1]	


def main():
	print "\t\t\t\tTablas de multiplicar\n"
	print "5 x 8 =",calcula(5,8),"\n"
	print "6 x 6 =",calcula(6,6),"\n"
	print "9 x 9 =",calcula(9,9),"\n"


if __name__=='__main__':
	main()
