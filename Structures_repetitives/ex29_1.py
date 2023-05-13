# Dans cette vidéo, nous allons écrire un programme qui demande un nombre positif non nul de départ, et qui calcule sa factorielle.
# Par exemple, la factorielle de 6, notée 6!, vaut 1 × 2 × 3 × 4 × 5 × 6.

# Procedure donner : 

def donner() :
    x = int(input("Donner un nombre factorielle :  "))
    while not(x >= 0) :
        x = int(input("Donner un nombre positif :  "))
    return(x)

# Fonction calcule :

def calcule(x) :
    s = 1
    for i in range (2,x+1) : 
        s = s * i
    return(s)

# Procedure afficher : 

def afficher() :
    print("Le resulta est = {:,d}".format(calcule(nb)))


# Algorithme pricipale : 

nb = donner()
afficher()