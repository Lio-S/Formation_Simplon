class Voiture():
    def __init__(self, marque, modèle, vitesse, moteur,couleur):
        self.__marque = marque
        self.__modèle = modèle
        self.__vitesse = vitesse
        self.__moteur = moteur
        self.__couleur = couleur

         ##################### Getter
        @property
        def marque() :
            print(f"G: La Marque de la voiture est {self.marque}")
            return self.__marque
        
        @property
        def modèle() :
            print(f"G: Le modèle de la voiture est {self.modèle}")
            return self.__modèle
        
        @property
        def vitesse() :
            print(f"G: La vitesse de la voiture est {self.vitesse}")
            return self.__vitesse
        
        @property
        def moteur() :
            print(f"G: Le moteur de la voiture est {self.moteur}")
            return self.__moteur
        
        @property
        def couleur() :
            print(f"G: La couleur de la voiture est {self.marque}")
            return self.__couleur
        
        ####################### Setter
        @marque.setter
        def marque(self, Marque_Test):
            print(f"S: La Marque de la voiture est {self.marque}")
            self.__marque = Marque_Test

        @modèle.setter
        def modèle(self, modèle_Test):
            print(f"S: Le modèle de la voiture est {self.modèle}")
            self.__modèle = modèle_Test

        @vitesse.setter
        def vitesse(self, vitesse_Test):
            print(f"S: La Marque de la voiture est {self.vitesse}")
            self.__vitesse = vitesse_Test
            
        @moteur.setter
        def moteur(self, moteur_Test):
            print(f"S: L moteur de la voiture est {self.marque}")
            self.__moteur = moteur_Test
            
        @couleur.setter
        def marque(self, couleur_Test):
            print(f"S: La Marque de la voiture est {self.couleur}")
            self.__couleur = couleur_Test
 
    def accélérer(self,pas):
        self.__vitesse += pas
 
    def afficher_vitesse(self):
        print(f"La vitesse de la voiture est de {self.__vitesse} km/h.")
 