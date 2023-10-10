'''9. Écrivez une fonction qui prend une liste de nombres en entrée 
    et renvoie une nouvelle liste contenant uniquement les nombres pairs de la liste initiale.'''

Indice=0
Combien_Nombre =int(input("Combien de nombre voulez-vous traiter ? "))
Nombres_Entrees=['0' for y in range(Combien_Nombre)]
Nombres_Pairs=[0 for y in range(Combien_Nombre)]

for i in range(Combien_Nombre):
    ret = int(input("Saisir un nombre : "))
    if (ret %2==0):
        Nombres_Pairs[Indice] = ret
        Indice +=1
# print(ret,i)
    else :
        del Nombres_Pairs[-1]

print("Les nombres pairs saisis sont : ",Nombres_Pairs)