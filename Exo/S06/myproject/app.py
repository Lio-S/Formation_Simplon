from components.mymodule import Voiture


ma_voiture = Voiture("Tesla", "Model S", 0, "électrique", "Jaune")
pas = 11
ma_voiture.accélérer(pas)
ma_voiture.afficher_vitesse()
pas = 111
ma_voiture.accélérer(pas)
ma_voiture.afficher_vitesse() 


###  Veille Streamlit