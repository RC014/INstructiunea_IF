"""
Se introduc vârstele a 3 persoane. 
Afişaţi vârstele cuprinse între 18 şi 60 de ani. 
Exemplu: Date de intrare 56  34  12  Date de ieşire  56  34.
"""

a=int(input("Introduceti varsta primei persoane:"))
b=int(input("Introduceti varsta celei de-a doua perosna:"))
c=int(input("Introduceti varsta celei de-a treia persoana:"))

if a>0 and b>0 and c>0:
    if a>18 and a<60:
        print(a)
    if b>18 and b<60:
        print(b)
    if c>18 and c<60:
        print(c)
    else: print("Nici-o persoana nu are varsta cuprinsa intre 18 si 60 de ani")

else: print("Una sau toate varstele introduse nu sunt valide")
