# Procedure saisie :
def saisie():
    while True:
        n = int(input("Donner un entier : "))
        if n >= 1:
            break
    return n

# fonction calcule :
def calcule(n):
    somme = 0
    for i in range(n):
        nombre_impair = 2 * i + 1
        carre = nombre_impair ** 2
        somme += carre
    return somme

# Procedure affichage :
def affichage():
    resultat = calcule(n)
    print("Le résultat est = {:,d}".format(resultat))

# Algorithme principal :
n = saisie()
affichage()
