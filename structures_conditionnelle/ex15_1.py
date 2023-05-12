# Dans cette vidéo, nous allons écrire un programme qui demande l’âge d’un enfant à l’utilisateur. Ensuite, il l’informe de sa catégorie : "Poussin" de 6 à 7 ans, "Pupille" de 8 à 9 ans, "Minime" de 10 à 11 ans, "Cadet" après 12 ans.

age = int(input("Donner l'age de l'enfant  :  "))

if 6 <= age <=7 :
    print("poussin")
elif 8 <= age <=9 :
    print("pupile")
elif 10 <= age <=11 :
    print("minime")
elif 12 <= age  :
    print("cadet")
else : 
    print("n'existe pas")
    

    