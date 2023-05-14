# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de taper un entier n, puis qui calcule la somme des carrées des n premiers entiers impairs. 

# il code hetha min inteji ena wa7di , w fih chab3a a8lat walli sal7ou w 5admou 


# Procedure saisie : 

def saisie() :
    while True :
        x = int(input("Donner un entier : "))
        if x >= 1 :
            break
    return(x)

# Procedure premiere :

def premiere(x) : 
    conteur = 1
    nb1 = 3
    T = [1]
    while not(conteur == x) : 
        premier = True
        for i in range (2,nb1) :
            if nb1 % i == 0 :
                premier = False
                break
        if premier :
            T.append(nb1)
            conteur += 1
        nb1 +=1
    return(T)

# Fonction somme_carrer : 

def somme_carrer() :
    somme = 0
    T1 = premiere(nb)
    for i in range (nb) :
        somme += T1[i]**2
    return(somme)

# Procedure affichage :

def affichage () : 
    print("Le resulta de {} nombre premier {} est = {}".format(len(premiere(nb)), premiere(nb), somme_carrer()))

# Algorithme pricipale : 

nb = saisie()
affichage()