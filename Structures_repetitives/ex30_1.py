# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de taper un entier n, puis qui calcule la somme des carrées des n premiers entiers impairs. 

# Procedure saisie : 

def saisie() :
    while True :
        x = int(input("Donner un entier : "))
        if x >= 1 :
            break
    return(x)

# foction calcule :

def calcule(x) : 
    conteur = 0
    nb1 = 2
    c1 = []
    while conteur < x : 
        est_premier = True
        for i in range (2,nb1) :
            if nb1 % i == 0 :
                est_premier = False
                break
        if est_premier :
            c1.append(nb1)
            conteur += 1
        nb1 +=1
    s = 0
    for i in range (i) : 
        s = (c1[i] == nb1)**2
    return(s)
                
        

# Procedure affichage :

def affichage () : 
    print("Le resulta est = {:,d}".format(calcule(nb)))

# Algorithme pricipale : 

nb = saisie()
affichage()