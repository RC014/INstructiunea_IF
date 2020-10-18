"""
La un concurs se dau ca premii primilor 100 de concurenţi, 
tricouri de culoare albă, roşie, albastră şi neagră, în această secvenţă. 
Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? 
Exemplu: date de intrare: x=38 date de ieşire: rosie. 
"""

x=int(input("Introduceti locul:"))

if x<=100:
    if x%4==0:
        print("neagra")
    elif x%3==0:
        print("albastra")
    elif x%2==0:
        print("rosie")
    else:
        print("alba")
else: print("Ion nu va primi nici-un premiu")