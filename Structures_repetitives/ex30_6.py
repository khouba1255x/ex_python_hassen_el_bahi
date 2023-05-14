
# il version hethi zeyda , just il chatgbt 9alli , hakka tawlli tsarri3 chway


# Procedure saisie :
def saisie():
    while True:
        x = int(input("Donner un entier : "))
        if x >= 1:
            break
    return x

# Procedure premier :
def premier(x):
    T = [1]
    conteur = 2
    nb1 = 3
    while not(conteur > x):
        est_premier = True
        for i in range(2, int((nb1**0.5)+1)) :
            if nb1 % i == 0:
                est_premier = False
                break
        if est_premier:
            T.append(nb1)
            conteur += 1
        nb1 += 2
    return T

# foction somme :

def somme() :
    s = 0
    T1 = premier(nb)
    for i in range (len(T1)) :
        s += T1[i]**2
    return(s)

# Procedure affichage : 

def affichage() :
    print("Les nombre premier sont {:d} : {} apres le calcule avec le puissance = {:d}".format(len(premier(nb)), premier(nb), somme() ))

# Algorithme pricipal :
nb = saisie()
affichage()