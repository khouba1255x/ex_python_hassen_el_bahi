# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de taper la largeur et la longueur d'un rectangle et qui en affiche le périmètre et la surface.
# le perimetre = المحيط

largeur = float(input("Donner largeur de la rectangle :  "))
longueur = float(input("Donner longueur de la rectangle :  "))

surface = largeur * longueur
perimetre = (largeur + longueur)*2

print("le surface =  {:.2f}".format(surface) )
print("le perimetre = {:.2f}".format(perimetre))