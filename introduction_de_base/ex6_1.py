# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de taper 5 notes et qui affiche leur somme et leur moyenne.

somme = 0
for i in range (5) :
    note = float(input("Donner le note nombre"+str(i+1)+" : "))
    somme = somme + note

moyenne = somme /5

print(f"le somme des notes sont {somme} et le moyenne = {moyenne} ")