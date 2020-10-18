import math
a=int(input("Introduceti valoarea pantei:"))
b=int(input("Introduceti valoarea coeficientului pe langa x:"))
c=int(input("Introduceti valoarea teremnului liber:"))

d=b**2-4*a*c
b = -b
if a>0 or a<0:
    if d>0:
        x01=(b- math.sqrt(d)) / (2*a)
        x02=(b+ math.sqrt(d)) / (2*a)
        print(x01, x02)
    elif d==0:
            x01=b / (2*a)
            print(x01)
    else:
        print("Ecuatia data nu are solutie")
else: print("Eroare:Introducet o ecuatie valida")