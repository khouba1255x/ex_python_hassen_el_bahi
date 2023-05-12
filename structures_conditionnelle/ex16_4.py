# Dans cette vidéo, nous allons écrire un programme permettant de saisir trois notes (sur 20) d'un étudiant, calculant sa moyenne et affichant cette moyenne avec la mention ("Très bien" à partir de 16, "Bien" entre 14 et 16, "Assez bien" entre 12 et 14, "Passable" entre 10 et 12, "Insuffisant" en dessous de 10)
#bil while : 

i = 1
totale = 0
notes_valides = 0

while i <= 3 and notes_valides < 3:
    note_i = int(input("Donner la note " + str(i) + " : "))
    if 0 <= note_i <= 20:
        totale += note_i
        notes_valides += 1
        i += 1
    else:
         note_i = int(input("Donner un vrai note " + str(i) + " : "))
         i += 1 

        
moyenne = totale / 3
print("La somme des notes valides est :", totale)

if moyenne >= 16:
    message = "Très bien"
elif 14 <= moyenne < 16:
    message = "Bien"
elif 12 <= moyenne < 14:
    message = "Assez bien"
elif 10 <= moyenne < 12:
    message = "Passable"
else:
    message = "Insuffisant"

print(message, " La moyenne est = {:.2f}".format(moyenne))

# hetha isle7 lil ex16_2
