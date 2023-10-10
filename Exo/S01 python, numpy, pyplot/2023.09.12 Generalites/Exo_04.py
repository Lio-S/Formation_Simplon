def Signe(nombre):
    nombre = input("Saisir nombre")
    if nombre == 0 : 
        print("Nombre nul")
    elif nombre < 0 : 
        print("Nombre Négatif")
    elif nombre > 0 : 
        print("Nombre Positif")
    else :
        print("Erreur")

Signe(nombre)