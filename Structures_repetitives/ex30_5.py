# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de taper un entier n, puis qui calcule la somme des carrées des n premiers entiers impairs.

# hetheya il version elli 9ad 9ad hiyya w il ex , m3a tasli7 8alta il 9 != un nombre premier , w m3aha il codition mta3 2!= un nombre impaire
# sall7t il syntaxe w ye5dem jawwou behy
 



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
        for i in range(2, nb1):
            if nb1 == 2 :
                est_premier = False
            elif nb1 % i == 0:
                est_premier = False
                break
        if est_premier:
            T.append(nb1)
            conteur += 1
        nb1 += 1
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






# hetha bish thabbit bih : 
# print("=" * 40)
# print(premier(nb))
# print("=" * 40)
# print(somme())