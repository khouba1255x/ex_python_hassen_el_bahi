# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur d'entrer un caractère et vérifie si le caractère donné est un alphabet, un nombre ou un caractère spécial.

# Procedure donner : 

def donner() :
    x = input("Donner un chifre ou un caractere  :  ")
    while not (len(x) == 1) :
        x = input("Donner un suel chifre ou un suel caractere  : ")
    return(x)


# fonction verifier :

def verifier(x) :
    if x.isdigit() and 0<= int(x) <=9: 
        message = "nombre"
    elif "A"<=x.upper()<="Z" : # dima ta3mel hakka w ella bil lower() w elle ta3mel double codition bish tajjem te5dem bi nafs il tari9a , w ella bil code acii
        message = "alphabet"
    else : 
        message = "caractere special"
    return(message)

# Procedure affichier :

def affichier() :
    print(f"Le caractere qui donner est un {verifier(A)}")


# Algorithme pricipale :

A = donner()
affichier()