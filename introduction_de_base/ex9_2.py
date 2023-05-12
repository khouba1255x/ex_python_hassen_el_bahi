# Dans cette vidéo, nous allons écrire un programme qui demande un temps T (entier) exprimé en secondes, et qui le convertit en heures, minutes, secondes.
#  Exemple : T = 56263 seconds =15 heures 37 minutes 43 seconds.

timeS = int(input("Donner un temps en seconde  :  "))

timeH = timeS//3600
timeM = (timeS % 3600)//60
timeS1 = (timeS % 3600) % 60

print("T  = {:,d} seconds  => {:d} heures  {:d} minutes  {:d} seconds".format(timeS, timeH, timeM, timeS1))

# fil version hethi sta3mlt il % fil 3amaliyyet