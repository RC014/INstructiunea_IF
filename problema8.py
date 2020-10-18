"""
Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. 
Exemple: Date de intrare 23  45Date de ieşire  nu exista numar par; 
Date de intrare  28 14  Date de ieşire 28;  
Date de intrare  77 4  Date de ieşire  4.
"""

a=int(input("Introduceti primul numar:"))
b=int(input("Introduceti al doilea numar:"))

if (a>b and a%2==0) or (a%2==0 and b%2!=0):
    print(a)
elif (a<b and b%2==0) or (b%2==0 and a%2!=0):
    print(b)
else: print("Nu exista numar par")