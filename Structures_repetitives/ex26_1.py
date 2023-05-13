# Dans cette vidéo, nous allons écrire un programme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants en utilisant la boucle while.
# Par exemple, si l'utilisateur entre le nombre 33, le programme affichera les nombres de 34 à 43. 

# nafs il ex mta3 ex25_1.py ama taw bil while 

def saisie() :
    x = int(input("Donner un nombre  :  "))
    return(x)
    
# Fonction repeter :

def repeter(x) : 
    i = 0
    while not(i ==10  ) :
        x = x+1
        print(str(i+1),"=",x,end="| ")
        i = 1+i

# Algorithme pricipale :

nb = saisie()
repeter(nb)