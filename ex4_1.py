# Dans cette vidéo, nous allons écrire un algorithme qui demande à l'utilisateur de saisir deux réels X et Y, et qui affiche la puissance X par Y.

x = float(input("Donner un reel x :  "))
y = float(input("Donner un reel y :  "))
r= x**y

print("le puissance y de x = {:.2f} ".format(r))