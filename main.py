from Member import Member
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet


pilote = Operator("khalil", "serdoun", "homme", 20, "pilote", 0)
technicien = Operator("charif", "Nom", "homme", 19, "technicien", 0)
khalil = Mentalist("khalil", "serdoun", "homme", 20, 100)

vaisseau1 = Spaceship("V1", "Destroyer", ['A', 'B', 'C'], "Prêt")
Flotte = Fleet("F1", [vaisseau1])

ma_flotte = Fleet("Enterprise Fleet", [])
# Avez-vous ajouté un vaisseau ?
v1 = Spaceship("Enterprise A", "Marchand", [], "Prêt")
ma_flotte.append_spaceship(v1)


""" vaisseau1.append_member(charif)
Flotte.append_spaceship(vaisseau1) """
v1.append_member(pilote)
v1.append_member(technicien)
ma_flotte.statistics()

""" for spaceship in Flotte._spaceships:
    print({spaceship._name})
for member in vaisseau1._crew:
    print({member._first_name})
 """
