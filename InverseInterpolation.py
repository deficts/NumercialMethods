import Bairstow as bstw
import LagrangeInterpolation as lagInt
import random

def inverseInterpolation(x,y,fx):
    polinomial=lagInt.crearPolinomio(x,y)
    polinomial.reverse()
    polinomial[0]=polinomial[0]-fx
    roots=[]
    r=random.random()
    s=random.random()
    bstw.bairstow(polinomial,r,s,roots)
    return roots
x=[1,2,3]
y=[3,2,1]

print(inverseInterpolation(x,y,4))
