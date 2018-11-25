#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Definición de las Funciones que se utilizarán en el Programa Principal
import MySQLdb
#ALEXANDRA
def introduce_total_alumnos():
	total=int(input("Introduce el número total de alumnos: "))
	while total<1 or total>5:
		total=int(input("\nError: El número total de alumnos debe estar entre 1 y 5. Vuelve a introducir el número total de alumnos: "))
	return total

def introduce_nombre_alumno(num_alumno,lista_nombres_alumnos):
	i=0
	nombre_alumno=[]
	print "ALUMNO NÚMERO ",num_alumno+1
	print "Introduce el alumno numero", num_alumno+1
	nombre_alumno=raw_input()
	#print range(len(lista_nombres_alumnos))
	while i<(len(lista_nombres_alumnos)):
		if lista_nombres_alumnos[i]==nombre_alumno:
			nombre_alumno=raw_input("Error: el alumno ya existe. Introduce el alumno nuevo :")
		i+=1
	return nombre_alumno
#ESTHER
def introduce_nota_alumno(num_alumno):
	i=0
	nota_alumno=float(input("Introduce la nota del alumno: "))
	print "La nota del alumno es: ",nota_alumno
	while nota_alumno<0 or nota_alumno>10:
			nota_alumno=float(input("Error: La nota debe estar entre 0 y 10. Introduce la nota del alumno: "))
	return nota_alumno

#PABLO	
def visualiza_alumno_mayor_nota(lista_nombres_alumnos, lista_notas_alumnos):
	posicion=0
	maximo=lista_notas_alumnos[0]
	for i in range(len(lista_notas_alumnos)):
		if lista_notas_alumnos[i]>maximo:
			maximo=lista_notas_alumnos[i]
			posicion=i
	print "El alumno ", lista_nombres_alumnos[posicion], "tiene la nota máxima, que es un ", maximo


#MARC PEREZ
def visualiza_alumno_menor_nota(lista_nombres_alumnos, lista_notas_alumnos):
	posicion=0
	minimo=lista_notas_alumnos[0]
	for i in range(len(lista_notas_alumnos)):
		if lista_notas_alumnos[i]<minimo:
			minimo=lista_notas_alumnos[i]
			posicion=i
	print "El alumno ", lista_nombres_alumnos[posicion], "tiene la nota mínima, que es un ", minimo

#DIEGO	
def calcula_num_aprobados(lista_nombres_alumnos, lista_notas_alumnos):
	aprobados=0
	lista_nombres_aprobados=[]
	lista_notas_aprobados=[]
	for i in range(len(lista_notas_alumnos)):
		if lista_notas_alumnos[i]>=5:
			lista_notas_aprobados+=[lista_notas_alumnos[i]]
			lista_nombres_aprobados+=[lista_nombres_alumnos[i]]
			aprobados+=1
	print "Hay ", aprobados, " alumnos aprobados"
	for i in range(len(lista_nombres_aprobados)):
		print lista_nombres_aprobados[i], " tiene una nota de ", lista_notas_aprobados[i], "\n"
		
#MARC ALVAREZ
def calcula_num_notables(lista_nombres_alumnos, lista_notas_alumnos):
	notables=0
	lista_nombres_notables=[]
	lista_notas_notables=[]
	for i in range(len(lista_notas_alumnos)):
		if lista_notas_alumnos[i]>=7 and lista_notas_alumnos[i]<9:
			lista_notas_notables+=[lista_notas_alumnos[i]]
			lista_nombres_notables+=[lista_nombres_alumnos[i]]
			notables+=1
	print "Hay ", notables, " alumnos con notable"
	for i in range(len(lista_nombres_notables)):
		print lista_nombres_notables[i], " tiene una nota de ", lista_notas_notables[i], "\n"

#ORIOL ÁLVAREZ
#Programa principal
lista_nombres_alumnos=[]
lista_notas_alumnos=[]
total_alumnos=0

total_alumnos=introduce_total_alumnos()

for i in range(total_alumnos):
	nombre_alumno=introduce_nombre_alumno(i,lista_nombres_alumnos)
	lista_nombres_alumnos+=[nombre_alumno]
	nota_alumno=introduce_nota_alumno(i)
	lista_notas_alumnos+=[nota_alumno]

#MIGUEL TRALLERO
#Menú de opciones
print "1.- Visualizar el alumno con mayor nota "
print "2.- Visualizar el alumno con menor nota "
print "3.- Calcular el número de Aprobados "
print "4.- Calcular el número de Notables "
print "5.- Salir "
opcion=input("Introduce la opción: ")
while opcion>=1 and opcion<5:
	if opcion==1:
		visualiza_alumno_mayor_nota(lista_nombres_alumnos, lista_notas_alumnos)
	elif opcion==2:
		visualiza_alumno_menor_nota(lista_nombres_alumnos, lista_notas_alumnos)
	elif opcion==3:
		calcula_num_aprobados(lista_nombres_alumnos, lista_notas_alumnos)
	elif opcion==4:
		calcula_num_notables(lista_nombres_alumnos, lista_notas_alumnos)
	opcion=input("Introduce la opción: ")



