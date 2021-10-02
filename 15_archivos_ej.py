# -*- coding: utf-8 -*-

##########################Ejercicio sobre archivos#########################
'''Ahora que ya sabe manejar archivos modificar el programa de tablas de
multiplicar hecho en el ejercicio 13 de tuplas para que ahora los resultados
 seanmandados a un archivo de texto'''


tabla = ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (2, 4, 6, 8, 10, 12, 14, 16, 18, 20), (3, 6, 9, 12, 15, 18, 21, 24, 27, 30), (4, 8, 12, 16, 20, 24, 28, 32, 36, 40), (5, 10, 15, 20, 25, 30, 35, 40, 45, 50), (6, 12, 18, 24, 30, 36, 42, 48, 54, 60), (7, 14, 21, 28, 35, 42, 49, 56, 63, 70), (8, 16, 24, 32, 40, 48, 56, 64, 72, 80), (9, 18, 27, 36, 45, 54, 63, 72, 81, 90), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100))


def calcula(n1, n2):
    return tabla[n1 - 1][n2 - 1]


def main():
    f = open("resultados.txt", "w")
    f.write("\t\t\tTablas de multiplicar\n")
    f.write("5 x 8 = " + str(calcula(5, 8)) + " \n")
    f.write("6 x 6 = " + str(calcula(6, 6)) + " \n")
    f.write("9 x 9 = " + str(calcula(9, 9)) + " \n")

    f.write("La diferencia entre una lista y una tupla es que las tuplas son inmutables y las listas no.")
    f = open("resultados.txt","r")
    print "El archivo resultados contiene lo siguiente: \n", f.read()
if __name__ == '__main__':
    main()

'''
#Manejando archivos

f = open("archivo.txt", "r") #Abriendo el archivo en modo lecurta

completo = f.read()           #devuelve una cadena con el contenido del archivo

f.close()                   #Cerrando el archivo

print completo

print "___"

f = open("archivo.txt", "r")

#Se lee el archivo línea por línea
while True:
      linea = f.readline()
      if not linea: break
      print linea

f.close()

print "___"


#Agragando una línea al archivo

otras_lineas=["otra linea 2 \n","otra linea 3 \n"]

f = open("archivo.txt", "a")
f.write("otra línea 1 \n")     #Guarda una línea
f.writelines(otras_lineas)     #Alamcena las líneas de una lista
f.close()


f = open("archivo.txt", "r")
lineas = f.readlines()    #Esta función lee las líneas y las almacena en una lista
f.close()

print lineas
'''
