# Dans cette vidéo, nous allons écrire un programme qui demande deux nombres entiers et l’une des opérateurs suivant : + , - , * , / puis effectue l’opération correspond et affiche le résultat de cette opération.


# Procedure Saisie : 

def saisie() :
    x = float(input("Donner un reel  : "))
    return(x)

# Fonction signe : 

def signe() : 
    s = input("Donner le signe arithmétique :  ")
    while not (s in ["-", "/", "*", "+"]) :
            s = input("Donner une vari signe arithmétique :  ")
    return(s)

# Fonction calcule : 

def calcule(nb1, S, nb2) :
    if  S == "+" :
        r = nb1 + nb2
    elif S == "-" :
        r = nb1 - nb2
    elif S == "*" : 
        r = nb1 * nb2
    elif S == "/" :
        if nb2 != 0 :
            r = nb1 / nb2
        else : 
            r = "La division par 0 est impossible "
    else :
        r = "Il ya un error"
    return(r)

# Procedure afficher :

def afficher () :
    print("le resulta est = {} ".format(calcule(nb1, S, nb2)))
    

# Algorithme principale :

nb1 = saisie()
S = signe()
nb2 = saisie()
afficher()