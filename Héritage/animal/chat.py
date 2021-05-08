# Importation des classes
from animal.animal import Animal

# Ma classe Chat hérite de la classe Animal
class Chat(Animal):

    # Constucteur de la classe Chat
    def __init__(self, nom, espece, couleur, pattes, queue):
        # Appel du constructeur de la classe mère (Animal)
        Animal.__init__(self, nom, espece, couleur)
        # Définition des autres attributs
        self.pattes = pattes
        self.queue = queue

    # Méthode miauler() pour faire miauler le chat
    def miauler(self):
        print("Miaou !")

    # Méthode marcher() pour faire marcher le chat
    def marcher(self, marche):
        if(marche):
            print("Le chat marche actuellement")
        else:
            print("Le chat ne marche pas actuellement")

    # Surcharge de la méthode afficherAnimal() pour l'adapter à la classe Chat
    def afficherAnimal(self):
        if(self.queue):
            texteQueue = "une queue"
        else:
            texteQueue = "n'a plus de queue"
        descriptionFinale = "Le chat", self.nom, "d'espèce", self.espece, "et de couleur", self.couleur, "a", str(self.pattes), "pattes et", texteQueue
        return " ".join(descriptionFinale)