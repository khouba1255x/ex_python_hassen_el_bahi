# Dans cette vidéo, nous allons écrire un programme qui demande un nombre positif non nul de départ, et qui calcule sa factorielle.
# Par exemple, la factorielle de 6, notée 6!, vaut 1 × 2 × 3 × 4 × 5 × 6.


while True : 
    n = int(input("Veuillez sasier la valeur de n : "))
    if n >= 0 : 
        break
if n == 0 : 
    print("La factorielle de 0 est 1 ")
else : 
    F = 1 
    for i in range (2, n+1) :
        F = F * i
    print("La factorielle de ",n,"est : ", F)