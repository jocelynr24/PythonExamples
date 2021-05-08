# Importation des classes
from animal.animal import Animal

# Ma classe Oiseau hérite de la classe Animal
class Oiseau(Animal):

    # Constucteur de la classe Oiseau
    def __init__(self, nom, espece, couleur, ailes):
        # Appel du constructeur de la classe mère (Animal)
        Animal.__init__(self, nom, espece, couleur)
        # Définition des autres attributs
        self.ailes = ailes

    # Méthode roucouler() pour faire roucouler l'oiseau
    def roucouler(self):
        print("Rhou !")

    # Méthode voler() pour faire voler l'oiseau
    def voler(self, vole):
        if(vole):
            print("L'oiseau vole actuellement")
        else:
            print("L'oiseau ne vole pas actuellement")

    # Surcharge de la méthode afficherAnimal() pour l'adapter à la classe Oiseau
    def afficherAnimal(self):
        descriptionFinale = "L'oiseau", self.nom, "d'espèce", self.espece, "et de couleur", self.couleur, "a", str(self.ailes), "ailes"
        return " ".join(descriptionFinale)