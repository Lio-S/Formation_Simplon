'''7. Écrivez une fonction qui prend une liste de nombres en entrée
     et renvoie la somme de tous les éléments de la liste.'''


Liste_Mots_Entrees=[]

for i in range(5):
    a = int(input("Saisir un nombre entiers : "))
    print(a)
    Liste_Mots_Entrees.append(a) 

print("La somme des nombres saisis est : ", sum(Liste_Mots_Entrees))