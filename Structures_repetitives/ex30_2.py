# il code hetha min 3and chatgbt 3andou meshekil  :
#       1: mea ye7sebch ra9m 1   
#       2: mea ya3milsh il 3dad puissansce 2
#       3: mea ye7sebsh il somme mta3 il A3ded elli na3tihelou

# il mashekil elli 7allitha : wa7di
#       1 : walla ye7seb il 1 fil list
#       2 : walla ya3mil  il 3dad puissansce 2
#       3 : walla ye7seb il somme mta3 il A3ded elli na3tihelou


# Procedure saisie :
def saisie():
    while True:
        x = int(input("Donner un entier : "))
        if x >= 1:
            break
    return x

# fonction premier :
def premier(x):
    c1 = [1]
    conteur = 1
    nb1 = 3
    while conteur < x:
        est_premier = True
        for i in range(2, nb1):
            if nb1 % i == 0:
                est_premier = False
                break
        if est_premier:
            c1.append(nb1)
            conteur += 1
        nb1 += 1
    return c1

# foction calcule : 
def calcule():
    somme = 0
    liste = premier(nb)
    for i in range (nb) :
        somme += liste[i]**2
    return(somme)
    
# Procedure affichage :
def affichage():
    resultat = premier(nb)
    print("Les {:d} premiers nombres premiers sont {} apres le calcule avec le puissance = {} :".format(len(resultat), premier(nb), calcule()))


# Algorithme pricipal :
nb = saisie()
affichage()

print("=" * 40)

# # testeur : 
# print(premier(nb))
# print(calcule())
