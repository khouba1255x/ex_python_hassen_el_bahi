# Procedure saisie :
def saisie():
    while True:
        x = int(input("Donner un entier : "))
        if x >= 1:
            break
    return x

# fonction premier :
def premier(x):
    c1 = []
    conteur = 0
    nb1 = 2
    while conteur < x:
        est_premier = True
        for i in range(2, nb1):
            if nb1 % i == 0:
                est_premier = False
                break
        if est_premier:
            c1.append(nb1)
            conteur += 1
        nb1 += 1
    return c1

# foction calcule : 
def calcule():
    resultat = premier(nb)
    s = sum([nombre ** 2 for nombre in resultat])
    return s
    

# Procedure affichage :
def affichage():
    resultat = premier(nb)
    print("Les {:,d} premiers nombres premiers sont :".format(len(resultat)))
    for nombre in resultat:
        print(nombre,end="+")

# Algorithme pricipal :
nb = saisie()
affichage()
