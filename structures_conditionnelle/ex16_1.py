# Dans cette vidéo, nous allons écrire un programme permettant de saisir trois notes (sur 20) d'un étudiant, calculant sa moyenne et affichant cette moyenne avec la mention ("Très bien" à partir de 16, "Bien" entre 14 et 16, "Assez bien" entre 12 et 14, "Passable" entre 10 et 12, "Insuffisant" en dessous de 10)

note = int(input("Donner le note : "))
while note<0 or note>20 : 
    note = int(input("Donner un vrai note : "))

if note >= 16 :
    print("Tres bien ")
elif 16 > note >= 14 : 
    print("Bien")
elif 14 > note >= 12 : 
    print("Assez bien ")
elif 12 > note >= 10 :
    print("Passable")
else : 
    print("Insuffisant")

# il version hethi te7seblik ken note wa7da