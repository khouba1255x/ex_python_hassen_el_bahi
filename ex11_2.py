# Dans cette vidéo, nous allons écrire un programme qui affiche la résistance équivalente à trois résistances R1, R2, R3 :
# - si les résistances sont branchées en série.
# # - si les résistances sont branchées en parallèle.

R1 = float(input("Donner la tension de resistence R1 :  "))
R2 = float(input("Donner la tension de resistence R2 :  "))
R3 = float(input("Donner la tension de resistence R3 :  "))

Rser = R1 + R2 + R3
Rpar = (R1 * R2 * R3)/(R1*R2+R1*R3+R3*R2)

print("Si les resistances sont branchees en serie {:.2f}".format(Rser))
print("Si les resistances sont branchees en parallele {:.2f}".format(Rpar))

# version te7seb kol chay