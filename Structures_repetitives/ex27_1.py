# Dans cette vidéo, nous allons écrire un programme qui calcule la somme des n premiers termes d’une série harmonique :     
# 𝒔 = 𝟏/𝟏+𝟏/𝟐+𝟏/𝟑+…+𝟏/𝒏 

# Procedure donner : 

def donner() : 
    x = int(input("Donner lengeur de la boucle :  "))
    return(x)

# Foction calcule :

def calcule(x) : 
    s = 0
    for i in range (1,x+1) :
        s = s + 1/i
    return(s)

# Procedure afficher : 

def afficher() : 
    print("le resulta est = {:.2f}".format(calcule(l)))
        

# Algorithme pricipale : 

l = donner()
afficher()