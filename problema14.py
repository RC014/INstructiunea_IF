"""
Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. 
Ionel  a  sosit  al  n-lea. În a câta căsuţă se va afla? 
Exemplu: date de intrare: n=69 date de ieşire: casuta 17.
"""

a=int(input("Al catelea a venit Ionel:"))
b=0
c=0
while c<a:
    c=c+4
    b=b+1
print(b)