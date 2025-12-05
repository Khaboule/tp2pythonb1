from Member import Member
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet

fleets = []
activ_fleet = None


def create_fleet():
    name_fleet = input("Quel est le nom de la nouvelle flotte ?")
    new_fleet = Fleet(name_fleet, [])
    fleets.append(new_fleet)
    print("Flotte '{name_fleet}' créée")
    return new_fleet

def choose_fleet():
    if len(fleets) == 0:
        print("Aucune flotte n'existe")
        return
    print("Flotte(s) disponible(s)")
    for i, fleets in enumerate(fleets, 1):
        nb_spaceships = len(fleets._spaceships)
        print(f"{i} {fleets._name} {nb_spaceships}")


print(f"\n[1] Ajouter une flotte")
print(f"\n[2] Modifier une flotte")
x = input("Quel est votre choix ?")
if x == 1:
    print("Création de la flotte")
    nouvelle_flotte = input("Quel est le nom de la nouvelle flotte ?")




while True:
    print("\n[1] Renommer la flotte")
    print("[2] Ajouter un vaisseau à la flotte")
    print("[3] Supprimer un vaisseau à la flotte")
    print("[4] Ajouter un membre d'équipage")
    print("[5] Supprimer un membre d'équipage")
    print("[6] Afficher les informations d'un équipage")
    print("[7] Vérifier la préparation d'un vaisseau")
    print("[8] Vérifier l'action d'un membre d'équipage")
    print("[9] Quitter\n")
    choice = input("Quel est votre choix ?")
    match choice:
        case "1":
        case "2":
            new_vaisseau = input("Quel est le nom du vaisseau ?")
        case "3":

        case "4":
            new_membre = input("Quel est le nom du nouveau membre")

        case _:
            break
