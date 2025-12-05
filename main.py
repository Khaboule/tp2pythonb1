from Member import Member
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
""" from Fleet import Fleet """


khalil = Member("khalil", "serdoun", "homme", 20)
khalil = Operator("khalil", "serdoun", "homme", 20, "pilote", 0)
khalil = Mentalist("khalil", "serdoun", "homme", 20, 100)
vaisseau1 = Spaceship("V1", "Destroyer", ['A', 'B', 'C'], "Prêt")


khalil.introduce_yourself()


