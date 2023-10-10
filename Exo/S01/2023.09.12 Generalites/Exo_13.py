# 13. Écrivez une fonction qui prend une chaîne de caractères en entrée 
# et renvoie le nombre de mots dans cette chaîne (un mot est séparé par un espace).

i=0

def Nombre_Mot():
    Chaine_En_Bordel= input("Tapez plusieurs mots séparés par un espace : ")
    for i in Chaine_En_Bordel:
        count = Chaine_En_Bordel.count(" ") + 1
    print(count)

Nombre_Mot()