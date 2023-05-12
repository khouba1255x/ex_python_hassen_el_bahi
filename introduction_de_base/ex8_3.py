# Dans cette vidéo, nous allons écrire un programme qui demande à l’utilisateur de saisir 2 entiers A et B, qui échange le contenu des variables A et B puis qui affiche A et B

A = int(input("Donner l'entier A  :  "))
B = int(input("Donner l'entier B  :  "))

A, B = B, A

print("le nombre A = {:d} et le nombre B = {:d}".format(A, B))

# lehneya baddilt il 5edma fil star we7id bark
