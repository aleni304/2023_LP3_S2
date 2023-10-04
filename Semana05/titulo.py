# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:51:00 2023

@author: Alumno
"""

#Importamos la librería
import camelcase

nombre = "alexia nicoll asunción pomasonco"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('alexia','pomasonco')
print(cam2.hump(nombre))



