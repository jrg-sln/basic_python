# -*- coding: utf-8 -*-

#####################Ejercicio sobre Lectura de archivos####################
'''Ahora que ya sabe capturar datos desde el teclado realice el ejercicio de
las tablas de multiplicar pero pidiendo los datos y adema´s ponga un menú'''

tabla = ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (2, 4, 6, 8, 10, 12, 14, 16, 18, 20), (3, 6, 9, 12, 15, 18, 21, 24, 27, 30), (4, 8, 12, 16, 20, 24, 28, 32, 36, 40), (5, 10, 15, 20, 25, 30, 35, 40, 45, 50), (6, 12, 18, 24, 30, 36, 42, 48, 54, 60), (7, 14, 21, 28, 35, 42, 49, 56, 63, 70), (8, 16, 24, 32, 40, 48, 56, 64, 72, 80), (9, 18, 27, 36, 45, 54, 63, 72, 81, 90), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100))


def calcula(n1, n2):
    return tabla[n1 - 1][n2 - 1]


def main():
    print "\t\t\t\tTablas de multiplicar\n"
    print "1. Hacer una multiplicación\n2. Salir\n"
    op = raw_input('Opción: ')
    while op == "1":
        n1 = raw_input('Primer número(1-10): ')
        n2 = raw_input('Segundo número(1-10): ')
        res = calcula(int(n1), int(n2))
        print n1, "x", n2, "=", res, "\n"
        print "1. Hacer una multiplicación\n2. Salir\n"
        op = raw_input('Opción: ')

if __name__ == '__main__':
    main()

'''La linea de arriba sirve para que no nos marque error con
   los acentos y los caracteres especiales

print "Hola, como te llamas?"
nombre = raw_input(' ')
print "Buen día " + nombre


running = True
while running:
    valor_1 = 0
    valor_2 = 0
    print "---Calculadora---"
    print "1- Sumar"
    print "2- Restar"
    print "3- Multiplicar"
    print "4- Dividir"
    print "5- Salir"
    op = int(raw_input('Opcion: '))
    if op == 1:
        print "---Sumar---"
        valor_1 = int(raw_input(''))
        print " + "
        valor_2 = int(raw_input(''))
        suma = valor_1 + valor_2
        print "El resultado es: %d" % suma
    elif op == 2:
        print "---Restar---"
        valor_1 = int(raw_input(''))
        print " - "
        valor_2 = int(raw_input(''))
        resta = valor_1 - valor_2
        print "El resultado es: %d" % resta
    elif op == 3:
        print "---Multiplicar---"
        valor_1 = int(raw_input(''))
        print " x "
        valor_2 = int(raw_input(''))
        multiplicacion = valor_1 * valor_2
        print "El resultado es: %d" % multiplicacion
    elif op == 4:
        print "---Dividir---"
        valor_1 = int(raw_input(''))
        print " / "
        valor_2 = int(raw_input(''))
        Dividir = valor_1 / valor_2
        print "El resultado es: %d" % Dividir
    elif op == 5:
        running = False
'''
