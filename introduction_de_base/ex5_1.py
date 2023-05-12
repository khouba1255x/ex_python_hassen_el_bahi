# Dans cette vidéo, nous allons écrire un programme opérations qui calcule la somme, le produit, la différence et la division de deux nombre réels.

nombre1 = float(input("Donner le nombre1 :  "))
operation = input("Donner une operation :  ")
nombre2 = float(input("Donner le nombre2 :  "))
print("Opération arithmétique {:.2f} {:s} {:.2f}".format(nombre1, operation, nombre2))


somme = nombre1 + nombre2
produit = nombre1 * nombre2
difference = nombre1 - nombre2
division = nombre1 / nombre2

if operation == "+" : 
    print(f"le somme de    {nombre1} + {nombre2} =",somme)
elif operation == "*" : 
    print(f"le produit de    {nombre1} * {nombre2} =",produit)
elif operation == "-" :
    print(f"le difference de    {nombre1} - {nombre2} =",difference)
elif operation == "/" :
    print(f"le division de    {nombre1} / {nombre2} =",division)
else : 
    print("Donner une vrai operetion")
    
# version hethi te7seb kol 7aja wa7idha 
