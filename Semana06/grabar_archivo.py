# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:28:17 2023

@author: Alumno
"""

archivo = open ("archivo_de_prueba.txt","wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a la Untels"
archivo.write(contenido)
archivo.close()

