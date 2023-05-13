# Dans cette vidéo, nous allons écrire un programme qui calcule et affiche la somme de la série :
# S = 1+10+100+…+10^n

# Procedure donner : 

def donner() :
    x = int(input("Donner le puissance  :  "))
    return(x)

# Fonction calcule : 

def calcule(x) :
    s = 0
    for i in range (x+1) :
        s = s + 10^i
    return(s)

# Procedure affichier : 

def affichier() : 
    print("Le resulta est  = {:d}".format(calcule(l)))


# Algorithme pricipale :

l = donner ()
affichier()