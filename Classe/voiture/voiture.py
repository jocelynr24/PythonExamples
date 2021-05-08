# Ma classe Voiture
class Voiture:

    # Constucteur de la classe voiture
    def __init__(self, marque, roues, couleur, vole):
        self.marque = marque
        self.roues = roues
        self.couleur = couleur
        self.vole = vole

    # Méthode afficherVoiture() pour afficher une description de la voiture
    def afficherVoiture(self):
        if(self.vole):
            texteVoler = "peut voler"
        else:
            texteVoler = "ne peut pas voler"
        descriptionFinale = "Ma voiture de marque", self.marque, "de couleur", self.couleur, "possède", str(self.roues), "roues et", texteVoler
        return " ".join(descriptionFinale)