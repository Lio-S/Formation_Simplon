def __init__(self, marque, modèle, vitesse, moteur):
        self.marque = marque
        self.modèle = modèle
        self.vitesse = vitesse
        self.moteur = moteur
 
    def accélérer(self):
        self.vitesse += 10
 
    def afficher_vitesse(self):
        print(f"La vitesse de la voiture est de {self.vitesse} km/h.")
 
ma_voiture = Voiture("Tesla", "Model S", 0, "électrique")
ma_voiture.accélérer()
ma_voiture.afficher_vitesse() # affiche "La vitesse de la voiture est de 10 km/h."
# Accélérer encore une 2 ème fois
ma_voiture.accélérer()
ma_voiture.afficher_vitesse() # affiche "La vitesse de la voiture est de 20 km/h."