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
    choice2 = int(input("\nQuelle flotte voulez vous sélectionner ?")) - 1
    if 0 <= choice2 < len(fleets):
        return fleets[choice2]
    else:
        print("Numéro invalide")
        return

while True:
    print("--- Gestion des flottes ---")
    print("[A] Créer une nouvelle flotte")
    print("[B] Sélectionner une flotte existante")
    print("[C] Supprimer une flotte")

    if activ_fleet:
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
        case "A":
            activ_fleet = create_fleet()
        case "B":
            selected_fleet = choose_fleet()
            if selected_fleet:
                activ_fleet = selected_fleet
        case "C":
            if len(fleets) == 0:
                print("Il n'y a aucune flotte à supprimer")
            else:
                for i, fleet_compteur in enumerate(fleets, 1):
                    print (f"[{i}], {fleet_compteur._name}")
                y = int(input("\nIndiquez le numéro de la flotte que vous voulez supprimer")) - 1
                if 0 <= y < len(fleets):
                    deleted_fleet = fleets.pop(y)
                    if activ_fleet == deleted_fleet:
                        activ_fleet = None
                else:
                    print("Numéro invalide")
        case "1":
        case "2":
            new_vaisseau = input("Quel est le nom du vaisseau ?")
        case "3":

        case "4":
            new_membre = input("Quel est le nom du nouveau membre")

        case _:
            break
