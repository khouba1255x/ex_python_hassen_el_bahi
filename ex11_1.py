# Dans cette vidéo, nous allons écrire un programme qui affiche la résistance équivalente à trois résistances R1, R2, R3 :
# - si les résistances sont branchées en série.
# # - si les résistances sont branchées en parallèle.

R1 = float(input("Donner la tension de resistence R1 :  "))
R2 = float(input("Donner la tension de resistence R2 :  "))
R3 = float(input("Donner la tension de resistence R3 :  "))

type = input("Donner le type de branchees les serie : en ")

Rser = R1 + R2 + R3
Rpar = (R1 * R2 * R3)/(R1*R2+R1*R3+R3*R2)

if type == "serie" :
    print("la tension equivalente  = {:.2f}".format(Rser))
elif type == "parallele" : 
    print("la tension equivalente  = {:.2f}".format(Rpar))
else : 
    print("donne un vrai type")

# version te7seb kol 7aja wa7idha 