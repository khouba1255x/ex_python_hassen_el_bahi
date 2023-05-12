# Dans cette vidéo, nous allons écrire un programme qui échange les contenus de deux données numérique si elles sont de même signe, sinon il met la somme des deux dans la première donnée et leur produit dans la seconde.

a = int(input("Donner un entier A :  "))
b = int(input("Donner un entier B :  "))

somme = a+b
prodauit = a*b

if a * b > 0 :
    a, b = b, a
    print("echange : ")
else :
    a = somme 
    b = prodauit
    print("somme et produit :  ")


print("La nouvelle valeur de A = {:d} la nouvelle valeur de B = {:d}".format(a, b))
