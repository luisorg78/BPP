import pytest
import unittest

# FUNCIONES
def cuadrado(n):
    return n*n

def factorial(n):
    if n==0:
        return 1
    else:
        aux=1
        for i in range (1,n+1):
            aux=aux*i
        return aux

def encuentra_maximo(n1, n2, n3):
    try:
        n1=float(n1)
        n2=float(n2)
        n3=float(n3)
        
        if (n1 >= n2) and (n1 >= n3):
            return n1
        elif (n2 >= n1) and (n2 >= n3):
            return n2
        else:
            return n3
    except ValueError:
        return "Debes introducir números"


    
