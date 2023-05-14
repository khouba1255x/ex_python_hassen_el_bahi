
# il code hetha min 3and chatgbt w ye5dew jawwou behy mea fih 7atta 8alta

# il version hethi copy , paste mil chatgpt , 9ad 9yes il ex , w bleash tasli7 a8lat


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
        print(nombre_impair,": nombre_impair|", somme,": somme|",carre,": carre")
    return somme

# Procedure affichage :
def affichage():
    resultat = calcule(n)
    print("Le résultat est = {:,d}".format(resultat))

# Algorithme principal :
n = saisie()
affichage()
print("=" *40)
print(calcule(n))
