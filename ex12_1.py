# Dans cette vidéo, nous allons écrire un programme qui retourne si deux nombres entiers donnés sont de même signe ou non.

a = float(input("Donner le nombre A  :  "))
b = float(input("Donner le nombre B  :  "))

if a<0 and b<0 :
    print("A et b on le meme signe  - ")
elif a>0 and b>0 :
    print("A et b on le meme signe  + ")
else : 
    print("A et B ont deux signes differents")
