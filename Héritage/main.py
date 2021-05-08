# Importation des classes
from animal.animal import Animal
from animal.chat import Chat
from animal.oiseau import Oiseau
from animal.poisson import Poisson


# Création d'une instance de chaque animal
monChat = Chat("Mistigri", "européen", "grise", 4, True)
monOiseau = Oiseau("Coco", "perroquet", "verte", 2)
monPoisson = Poisson("Némo", "poisson rouge", "rouge")
# Le chien n'étant pas disponible, on le créé en tant qu'animal générique
monChien = Animal("Doggy", "Labrador", "beige")

# Description initiale des animaux
print(monChat.afficherAnimal())
print(monOiseau.afficherAnimal())
print(monPoisson.afficherAnimal())
print(monChien.afficherAnimal())
input()

# Utilisation des méthodes
monChat.marcher(True)
monChat.miauler()
monChat.manger("pâtée", "féminin")
input()

monOiseau.voler(False)
monOiseau.roucouler()
monOiseau.manger("morceau de pain", "masculin")
input()

monPoisson.nager(True)
input()

monChien.manger("croquette", "féminin")
input()

# Malheureusement, mon chat a perdu sa queue...
monChat.queue = False
print(monChat.afficherAnimal())