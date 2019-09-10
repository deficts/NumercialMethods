#Metodo de Bairstow implementado por Diego Arredondo A01633932 y Santiago Aragon A01634433
import cmath
import random

#Formula general de la forma ax^2+bx+c
def chicharronera(a,b,c):
    discriminante = b**2.0 - 4.0*a*c
    if discriminante > 0:
        rdiscriminante = cmath.sqrt(discriminante)
        x1 = (-b + rdiscriminante )/(2*a)
        x2 = (-b - rdiscriminante )/(2*a)
        return [(x1,0),(x2,0)]
    if discriminante == 0:
        x = -b / (2*a)
        return [(x,0),(x,0)]
    xr = -b / (2*a)
    xi = cmath.sqrt(abs(discriminante)) / (2*a)
    return [(xr,xi),(xr,-xi)]

#Funcion de preparacion
def bairstow(a,r,s,roots):
    bairstowG(a,r,s,len(a)-1,roots)

def bairstowG(a,r,s,g,roots):
    if(g<1):
        return None
    if(g==1):
        roots.append(float(-a[0])/float(a[1]))
        return None
    if(g==2):
        roots.append(chicharronera(a[2],a[1],a[0])[0])
        roots.append(chicharronera(a[2],a[1],a[0])[1])
        return None
    n = len(a)
    b = [0]*len(a)
    c = [0]*len(a)
    b[n-1] = a[n-1]
    b[n-2] = a[n-2] + r*b[n-1]
    i = n - 3
    while(i>=0):
        b[i] = a[i] + r*b[i+1] + s*b[i+2]
        i = i - 1
    c[n-1] = b[n-1]
    c[n-2] = b[n-2] + r*c[n-1]
    i = n - 3
    while(i>=0):
        c[i] = b[i] + r*c[i+1] + s*c[i+2]
        i = i - 1
    Din = ((c[2]*c[2])-(c[3]*c[1]))**(-1.0)
    r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
    s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
    if(abs(b[0])>1E-8 or abs(b[1])>1E-8):
        return bairstowG(a,r,s,g,roots)
    if (g>=3):
        roots.append(chicharronera(1.0,-r,-s)[0])
        roots.append(chicharronera(1.0,-r,-s)[1])
        return bairstowG(b[2:],r,s,g-2,roots)

g=int(input("Ingresa el grado de tu polinomio:\n"))+1
a=[]
for i in range(g):
    a.append(int(input("Ingresa el valor con grado "+str(i)+"\n")))
c=0
r = random.random()
s = random.random()
roots=[]
bairstow(a,r,s,roots)
print("\nRaices de")
for i in range(g):
    print(str(a[g-1-i])+"x^"+str(g-1-i))
for r in roots:
  print("R" + str(c) + " = " + str(r))
  c += 1

'''
c=0
roots = []
parametros de est forma 1+x-2x^2+3x^3-4x^4+5x^5-6x^6
a = [1,+1,-2,+3,-4,+5,-6]
r = random.random()
s = random.random()
bairstow(a,r,s,roots)
print("\nRaices => \n")
for r in roots:
  print("R" + str(c) + " = " + str(r))
  c += 1
'''
