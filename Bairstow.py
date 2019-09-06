#Metodo de Bairstow implementado por Diego Arredondo A01633932 y Santiago Aragon A01634433
import cmath

#def bairstow():


#Formula general de la forma ax^2+bx+c
def chicharronera(a,b,c):
    d=(b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return [sol1,sol2]

print(chicharronera(1,5,6))
