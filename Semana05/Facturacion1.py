# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:36:45 2023

@author: Alumno
"""

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal):.2f}")
