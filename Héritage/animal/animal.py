# Ma classe Animal
class Animal:

    # Constucteur de la classe Animal
    def __init__(self, nom, espece, couleur):
        self.nom = nom
        self.espece = espece
        self.couleur = couleur

    # Méthode manger() prenant pour paramètres le nom de l'aliment et le genre (masculin ou féminin) de l'aliment
    def manger(self, aliment, genre):
        if(genre == "masculin"):
            print("Notre animal mange un", aliment)
        elif(genre == "féminin"):
            print("Notre animal mange une", aliment)

    # Méthode afficherAnimal() pour afficher des informations générales d'un animal
    def afficherAnimal(self):
        descriptionFinale = "L'animal", self.nom, "d'espèce", self.espece, "est de couleur", self.couleur
        return " ".join(descriptionFinale)