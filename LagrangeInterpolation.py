from sympy import *
import matplotlib.pyplot as plt
import numpy as np

#Recibimos dos arreglos con los valores de x & y
def crearPolinomio(x,y):
    n=len(x)
    polinomio=''
    #Recorremos los arreglos para generar la expresion en string de la sumatoria de la forma
    #(x-xj)/(xi-xj)
    for i in range(n):
        polinomio+= str(y[i])+'* ('
        denominador=1
        for j in range(n):
            if(j==i):
                continue
            polinomio+='(x - %f)*'%(x[j])
            denominador*=x[i]-x[j]
        polinomio=polinomio[:-1] + '/%f) +'%(denominador)
    polinomio=polinomio[:-1]
    #Pasamos la expresion a sympy para ser simplificada y expandida
    polinomio=sympify(polinomio)
    polinomio=expand(polinomio)
    #Regresamos el polinomio creado
    return poly(polinomio).coeffs()
