# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:57:56 2023

@author: Alumno
"""
import os

#Declaración de funciones
def crear_archivo(nombre,contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()
    
def eliminar_archivo(nombre):
    os.remove(nombre)
    
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write("\n" + contenido)
    archivo.close()
    
def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding="utf8")
    contenido = archivo.read()
    return contenido