'''6. Écrivez un programme qui demande à l'utilisateur de saisir 5 nombres entiers, acquisition clavier, 
    les stocke dans une liste, puis affiche la liste.'''

Liste_Mots_Entrees=[]

for i in range(5):
    a = int(input("Saisir un nombre entiers : "))
    print(a)
    Liste_Mots_Entrees.append(a) 

print("La liste des nombres saisis est : ",Liste_Mots_Entrees)


