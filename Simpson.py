#By Diego Arredondo Reyes A01633932 and Santiago Aragon Sanchez A01634433

def simpson38(h,f0,f1,f2,f3):
    return (3/8)*h*(f0+3*f1+3*f2+f3)

def simpson13(h,n,f):
    sum=f[0]
    for i in range(1,n-2,2):
        sum=sum+4*f[i]+2*f[i+1]
    sum=sum+4*f[n-1]+f[n]
    return(h/3)*sum

def intsim(a,b,n,f):
    h=(b-a)/n
    sum=0
    if n==1:
        sum=(h/2)*(f[n-1]+f[n])
    else:
        m=n
        odd=n%2
        if odd>0 and n>1:
            sum=sum + simpson38(h,f[n-3],f[n-2],f[n-1],f[n])
            m=n-3
        if m>1:
            #print("and this is crazy")
            sum=sum+simpson13(h,m,f)
            #print(sum)
    return sum

def simpson(a):
    if(len(a)<1 and len(a[0][1])<1):
        return -1
    return intsim(a[0][0],a[0][len(a[0])-1],len(a[0])-1,a[1])

a=[[-3,-1,1,3,5],[-3375,-343,1,729,4913]]

b=[[-3,-1.4,0.2,1.8,3.4,5],[-3375,-636.056,-10.648,74.088,1191.02,4913]]

print(simpson(a))

print(simpson(b))
