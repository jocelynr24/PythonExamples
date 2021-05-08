# Importation des classes
from animal.animal import Animal

# Ma classe Poisson hérite de la classe Animal
class Poisson(Animal):

    # Constucteur de la classe Oiseau
    def __init__(self, nom, espece, couleur):
        # Appel du constructeur de la classe mère (Animal)
        Animal.__init__(self, nom, espece, couleur)

    # Méthode nager() pour faire nager le poisson
    def nager(self, nage):
        if(nage):
            print("Le poisson nage actuellement")
        else:
            print("Le poisson ne nage pas actuellement")

    # Surcharge de la méthode afficherAnimal() pour l'adapter à la classe Poisson
    def afficherAnimal(self):
        descriptionFinale = "Le poisson", self.nom, "d'espèce", self.espece, "est de couleur", self.couleur
        return " ".join(descriptionFinale)