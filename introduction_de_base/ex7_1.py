# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de taper le rayon d’une sphère, puis calcule et affiche son volume.

from math import pi

rayon = float(input("Donner le rayon de la sphere :  "))
calcule = (4*pi*rayon**3)/3

print("Volume d'une shpere = {:.2f}".format(calcule))