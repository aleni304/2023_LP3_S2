# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:54:20 2023

@author: Alumno
"""

archivo = open("noticia.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: RPP"

archivo.write(contenido)

archivo.close()
