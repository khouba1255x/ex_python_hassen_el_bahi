# Dans cette vidéo, nous allons écrire un programme qui résout le problème suivant : 
# La population de la ville de Marrakech est de 1, 000, 000 d’habitants et elle augmente de 50, 000 habitants par an. Celle de la ville d'Agadir est de 500, 000 habitants et elle augmente de 8% par an. Écrire un programme permettant de déterminer dans combien d’années la population de la ville d'Agadir dépassera celle de la ville de Marrakech.

# mel9itish famma leazma lil algorithme pricipale , w lil commits kima mestenis
# version 2 ba3d mea tfarrijt fil tafsir
marrakech = 3000000
agadir = 500000
annee = 2023
while not(marrakech < agadir ) :
    marrakech += 50000
    agadir = agadir* 1.08
    annee += 1

print("Agadir depassera Marrakech dans {:d} apres {:d} ans".format(annee, annee - 2023 ))
print("Marrakech = {:.0f} et Agadir = {:.0f}".format(marrakech, agadir))