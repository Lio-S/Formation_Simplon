# 10 Écrivez un programme qui prend une liste de mots en entrée, 
#       acquisition clavier, les trie par ordre alphabétique 
#        et affiche la liste triée

Liste_Mots_Entrees=[]
Nombre_De_Mot = int(input("Nombre de mot à traiter : ?"))

for i in range(Nombre_De_Mot):
    a = input("Saisir un mot:")
    print(a)
    Liste_Mots_Entrees.append(a) 


Liste_Mots_Entrees.sort()

print("La liste triée par ordre alphabétique est : ",Liste_Mots_Entrees)