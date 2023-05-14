# Dans cette vidéo, nous allons écrire un programme qui affiche les diviseurs d’un entier positif n non nul.
# with for

# Procedure donner : 

def donner() : 
    while True : 
        x = int(input("Donner un entier pour fait une division :  "))
        if x !=0 :
            break
    return(x)

# Procedure division : 

def division(nb) :
    conteur = 1
    T = []
    for i in range (1,(nb//2)+1) : 
        if nb % i == 0 :
            conteur += 1
            T.append(i)
    T.append(nb)
    return("Nombre les entier = {} sont : {}".format(conteur, T))


# Algorithme pricipale : 

nb  = donner()
print(division(nb))