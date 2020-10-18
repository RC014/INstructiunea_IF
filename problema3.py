"""
Să se verifice dacă o literă introdusă este vocală sau consoană. 
Exemplu: Date de intrare  a  Date de ieşire   vocala.
"""

a=input("Introduceti litera:")

if a in ["a", "e", "i", "o", "u", "ă", "î", "â"]:
    print("Vocala")

elif a in ["b", "c", "d", "f", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "ș", "t", "ț", "v", "w", "x", "z", "y"]:
    print("Consoana")

else:
    print("Caracterul introdus nu este litera")