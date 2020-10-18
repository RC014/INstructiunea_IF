"""
Pe o masă de biliard sunt bile albe, roşii şi verzi. 
Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. 
Să se afişeze câte bile sunt în total pe masa de biliard. 
Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând numărul lor. De ce culoare sunt bilele cele mai numeroase? 
Precizaţi numărul lor. 
Exemplu: Date de intrare  
Nr. bile albe mici: 2 
Nr. bile albe mari: 3 
Nr. bile rosii mici: 1 
Nr. bile rosii mari: 4 
Nr. bile verzi mici: 3 
Nr. bile verzi mari: 4  
Date de ieşire 
Totalul bilelor: 17   Mari: 11 bile    Verzi: 7 bile .
"""

ami=int(input("Nr. bile albe mici:"))
ama=int(input("Nr. bile albe mari:"))
rmi=int(input("Nr. bile rosii mici:"))
rma=int(input("Nr. bile rosii mari:"))
vmi=int(input("Nr. bile verzi mici:"))
vma=int(input("Nr. bile verzi mari:"))

print("Totalul bilelor:",ami+ama+rmi+rma+vmi+vma)
print("Mari:",ama+rma+vma,"bile")

if ami>=0 and ama>=0 and rmi>=0 and rma>=0 and vmi>=0 and vma>=0:
    if ami+ama>rmi+rma and ami+ama>vmi+vma:
        print("Albe:", ami+ama,"bile")
    elif rmi+rma>ami+ama and rmi+rma>vmi+vma:
        print("Rosii:",rmi+rma,"bile")
    elif vmi+vma>rmi+rma and vmi+vma>ama+ami:
        print("Verzi:",vmi+vma)
    elif ami+ama==rmi+rma and ami+ama>vmi+vma:
        print("Albe si rosii a cate",ami+ama,"bile")
    elif ami+ama==vmi+vma and ami+ama>rmi+rma:
        print("Albe si verzi a cate",ami+ama,"bile")
    elif rmi+rma==vmi+vma and rmi+rma>ama+ami:
        print("Rosii si verzi a cate",rmi+rma,"bile")
    elif ami+ama==rmi+rma and ami+ama==vmi+vma:
        print("Numarul bilelor de fiecare culoare este egal")
else: print("Eroare:Nu puteti fi dator cu bile")