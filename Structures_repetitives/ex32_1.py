# Dans cette vidéo, nous allons écrire un programme qui résout le problème suivant : 
# A la naissance de Amal, son grand-père Ali, lui ouvre un compte bancaire. Ensuite, à chaque anniversaire, le grand père d' Amal verse sur son compte 500 dh, auxquels il ajoute le triple de l’âge de Amal. Par exemple, lorsqu’elle a quatre ans, il lui verse 512 dh. Écrire un programme qui permette de déterminer quelle somme aura Amal lors de son nième anniversaire. 

# Procedure donner : 

def donner() : 
    while True : 
        age = int(input("Donner l'age de Amal  : "))
        if age > 0 : 
            break
    return(age)

# Fonction somme : 

def somme() : 
    s = 0
    for i in range (1, age+1) : 
        s += 500 + i * 3 
    return("Amal à 5 ans et le totale dans le compte est {:,d} dh".format(s))
    


# Algorithme principale : 

age = donner()
print(somme())