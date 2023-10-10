# 5. Écrivez un programme qui demande à l'utilisateur de saisir un mot
#     et affiche si ce mot contient plus de 5 caractères.

a = input("Saisir un mot : ")
if len(a)>5 :
    print("Ce mot contient plus de 5 caractères")
elif len(a)==5 :
    print("Ce mot contient 5 caractères")
else :
    print("Ce mot contient moins de 5 caractères")