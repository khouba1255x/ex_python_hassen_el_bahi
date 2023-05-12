# Dans cette vidéo, nous allons écrire le programme suivant : Un magasin facture 0,30 dh les dix premières photocopies, 0,25 dh les vingt suivantes et 0,20 dh au-delà. Ecrire un programme qui demande à l’utilisateur le nombre de photocopies effectuées et qui affiche la facture correspondante.

nb = int(input("Donner le nombre des photocopies  :  "))

if nb <= 10 :
    montant = nb * 0.30
elif 11<= nb <= 20 :
    montant = (10 * 0.30) + (nb - 10) * 0.25
else : 
    montant = (10 * 0.30) + (10 * 0.25) + (nb - 20) * 0.20

print("Le totale de ces photocopies est = {:.2f}".format(montant))

# il version hethi , te5dem il promotion ken bil 10 bil 10 