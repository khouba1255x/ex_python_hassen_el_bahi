# Dans cette vidéo, nous allons écrire un programme qui demande l’âge et le sexe d’un habitant et affiche si celui-ci est imposable

# paient = يدفع الضرائب
# affiche si celui-ci est imposable = يعرض ما إذا كان خاضعًا للضريبة

age = int(input("Donner l'age  :  "))
sexe = input ("Donner le sexe , homme ou famme  :  ")

paient = "ne paient pas"
if (sexe == "homme" and age >= 20) or (sexe == "famme" and 18<= age <= 35) :
    paient = "paient"
else :
    paient = "ne paient pas"

print("tu as",paient,"tan taxe")
