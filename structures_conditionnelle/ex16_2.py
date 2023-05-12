# Dans cette vidéo, nous allons écrire un programme permettant de saisir trois notes (sur 20) d'un étudiant, calculant sa moyenne et affichant cette moyenne avec la mention ("Très bien" à partir de 16, "Bien" entre 14 et 16, "Assez bien" entre 12 et 14, "Passable" entre 10 et 12, "Insuffisant" en dessous de 10)
#bil while : 

i = 1
totale = 0
note_i = int(input("Donner le notes  "+str(i)+" : "))
while not(10<=note_i<=20) and not (i>4)  : 
    note_i = int(input("Donner un vrai notes "+str(i)+" : "))
    totale = totale + note_i
    i = i+1
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

print(message, " le moyenne est = ", moyenne)

# le9i moshkla enni kol mea na3mel 7aja 8alta fi wist il input elli tebi3 il while ye7sebha w il i t9addem w il totale tzid

