# Dans cette vidéo, nous allons écrire un programme qui affiche la ou les solutions d’une équation du second degré de la forme ax² + bx + c = 0. 

a = float(input("Donner le reel a :  "))
b = float(input("Donner le reel b :  "))
c = float(input("Donner le reel c :  "))

from math import sqrt


Sr = 0
delta = b**2 - 4*a*c

if delta < 0 :
    Sr = "n'a pas de solution"
elif delta == 0 : 
    Sr = -b/(2*a)
elif delta > 0 :
    Sr = (-b -sqrt(delta))/(2*a) , (-b +sqrt(delta))/(2*a) 
else : 
    print(" il y a in probleme dans cette equiation")

print("les solution de equiation {:.2f}x² + {:.2f}x +{:.2f} =  {}".format(a, b, c, Sr))