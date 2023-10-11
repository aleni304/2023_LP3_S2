# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:04:49 2023

@author: Alumno
"""

import gestion_archivos

def menu():
    print("\n**** MENÚ PRINCIPAL ****")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar contenido del archivo")
    print("5. Salir")

def crear():
    print("\n -- CREAR ARCHIVO -- ")
    archivo = input("Nombre del archivo: ")
    contenido = input("Contenido del archivo: ")
    gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("\n -- ELIMINAR ARCHIVO -- ")
    archivo = input("Nombre del archivo: ")
    gestion_archivos.eliminar_archivo(archivo)

def agregar():
    print("\n -- AGREGAR DATOS A UN ARCHIVO -- ")
    archivo = input("Nombre del archivo: ")
    contenido = input("Contenido a agregar: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("\n -- MOSTRAR CONTENIDO DE ARCHIVO -- ")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo))

def salir():
    print("Gracias por su visita...")

def error():
    print("Opción incorrecta")

opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("Opción: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
    
    