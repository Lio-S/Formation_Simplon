'''8. Écrivez une fonction qui prend une liste de mots en entrée
     et renvoie une nouvelle liste contenant la longueur de chaque mot.'''

Nombre_Mot =int(input("Saisir le nombre de mot souhaités : "))
Liste_Mots_Entrees=['0' for y in range(Nombre_Mot)]
Longueur_Mots=[0 for y in range(Nombre_Mot)]

for i in range(Nombre_Mot):
    Liste_Mots_Entrees[i] = input("Saisir un mot : ")
    Longueur_Mots[i]  = len(Liste_Mots_Entrees[i])

print("La longueur de chaque mot saisi est : ",Longueur_Mots)