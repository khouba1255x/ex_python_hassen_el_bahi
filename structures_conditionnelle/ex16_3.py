# Dans cette vidéo, nous allons écrire un programme permettant de saisir trois notes (sur 20) d'un étudiant, calculant sa moyenne et affichant cette moyenne avec la mention ("Très bien" à partir de 16, "Bien" entre 14 et 16, "Assez bien" entre 12 et 14, "Passable" entre 10 et 12, "Insuffisant" en dessous de 10)
#bil while : 


totale = 0
for i in range (3) :
    note_i = int(input("Donner un notes "+str(i+1)+" : "))
    while not(0<=note_i<=20)  : 
        note_i = int(input("Donner un vrai notes "+str(i+1)+" : "))
    totale = totale + note_i
    
moyenne = totale /3
print(totale)

if moyenne >= 16 :
    message = "Tres bien "
elif 16 > moyenne >= 14 : 
    message = "Bien"
elif 14 > moyenne >= 12 : 
    message = "Assez bien "
elif 12 > moyenne >= 10 :
    message = "Passable"
else : 
    message = "Insuffisant"

print(message, " le moyenne est = {:.2f}".format(moyenne))
