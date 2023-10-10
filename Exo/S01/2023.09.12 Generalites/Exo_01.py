# Nombre entier positif
Nb_Entier_Pos = int(input("Saisir un nombre entier positif"))
i = 1
while i-1 < Nb_Entier_Pos :
# print(i) if Nb_Entier_Pos > 0 else Nb_Entier_Pos -= -1
    if int(Nb_Entier_Pos) > 0 :
        print(i)
        i+= 1
    else : Nb_Entier_Pos -= -1