# Dans cette vidéo, nous allons écrire un programme qui calcule et affiche la distance entre deux pofloats A et B du plan dont les coordonnées (XA , YA) et (XB , YB) sont entrées au clavier comme entiers. 

from math import sqrt

Xa = float(input("Donner Xa  :  "))
Xb = float(input("Donner Xb  :  "))
Ya = float(input("Donner Ya  :  "))
Yb = float(input("Donner Yb  :  "))

ab = sqrt((Xb - Xa)**2 + (Yb - Ya)**2)

print("Le distance entre A est B =  {:.2f}".format(ab))
