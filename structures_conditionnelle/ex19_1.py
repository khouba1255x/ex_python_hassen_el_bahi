# Dans cette vidéo, nous allons écrire un programme qui calcule le prix TTC d’un produit connaissant son prix hors taxe et sa catégorie

PHT = float(input("Donner le prix avant les taxe en DT :  "))
categorie = input("Donner le categorie de le produit (A, B or C) :  ")

PTTC = 0
if categorie == "A" : 
    PTTC = PHT +  PHT * 0.07
elif categorie == "B" :
    PTTC = PHT + PHT * 0.2
elif categorie == "C" :
    PTTC = PHT + PHT * 0.25
else : 
    print("Donner une vaie categorie")
    
print("Le PTTC  = {:.2f} DT".format(PTTC))