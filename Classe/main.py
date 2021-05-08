# Importation des classes
from voiture.voiture import Voiture


# Déclaration et instanciation des voitures
maVoitureModerne = Voiture("Renault", 4, "bleue", False)
maVoitureDuFutur = Voiture("Renault", 0, "blanche", True)

# Utilisation des méthodes
description = maVoitureModerne.afficherVoiture()
print(description)
description = maVoitureDuFutur.afficherVoiture()
print(description)