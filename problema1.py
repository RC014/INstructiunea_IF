"""
Se introduc trei date de forma număr curent elev, punctaj. 
Afişaţi numărul elevului cu cel mai mare punctaj. 
Exemplu: Date de intrare  nr crt  7  punctaj 120  nr crt  3  punctaj 100 nr crt 4 punctaj 119  Date de ieşire  punctaj maxim areelevul cu nr crt 7.
"""
n1=int(input("Introduceti numarul curent al elevului:"))
print("Introduceti punctajul elevului nr.", n1,":")
p1=int(input())

n2=int(input("Introduceti numarul curent al elevului:"))
print("Introduceti punctajul elevului nr.", n2,":")
p2=int(input())

n3=int(input("Introduceti numarul curent al elevului:"))
print("Introduceti punctajul elevului nr.", n3,":")
p3=int(input())


if p1>p2 and p1>p3:
    print("Punctaj maxim are elevul cu numarul",n1)

elif p2>p1 and p2>p3:
    print("Punctaj maxim are elevul cu numarul",n2)

elif p3>p1 and p3>p2:
    print("Punctaj maxim are elevul cu numarul",n3)
    
elif p1==p2 and p2==p3:
    print("Error")

elif p1==p2 and p1>p3:
    print("Error")

elif p1==p3 and p1>p2:
    print("Error")

elif p2==p3 and p2>p1:
    print("Error")

else:
    print("Error")
