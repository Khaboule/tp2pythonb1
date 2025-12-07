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
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                new_fleet_name = input("Entrez le nouveau nom")
                activ_fleet._name = new_fleet_name
        case "2":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                new_spaceship_name = input("Quel est le nom du vaisseau ?")
                new_spaceship_type = input("Quel est le type du vaisseau ?")
                new_spaceship = Spaceship(new_spaceship_name, new_spaceship_type)
                activ_fleet.append(new_spaceship)
        case "3":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship._name}")
                b = int(input("Choisissez le numéro du vaisseau à supprimer"))
                if 0 <= b < len(activ_fleet._spaceships):
                    deleted_spaceship = activ_fleet._spaceships.pop(b)
                else:
                    print("Numéro invalide")
        case "4":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship._name}")
                c = int(input("Choisissez le numéro du vaisseau où le nouveau membre sera déployé"))
                if 0 <= c < len(activ_fleet._spaceships):
                    choosed_spaceship = activ_fleet._spaceships[c]
                    print("\nType de membre:")
                    print("[1] Opérateur")
                    print("[2] Mentaliste")
                    print("[3] Membre de base")
                    type_member = input("Choisissez le type du nouveau membre")
                    first_name = input("Prénom:")
                    last_name = input("Nom:")
                    sexe = input("Genre:")
                    age = input("Age:")
                    if type_member == 1:
                        role = input("Choisissez le rôle (technicien/pilote/navigateur/médecin/ingénieur)")
                        new_member = Operator(first_name, last_name, sexe, age, role)
                    elif type_member == 2:
                        new_member = Mentalist(first_name, last_name, sexe, age)
                    else:
                        new_member = Member(first_name, last_name, sexe, age)

                    choosed_spaceship.append_member(new_member)
                else:
                    print("Numéro invalide")
        case "5":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship._name}")
                d = int(input("Choisissez le numéro du vaisseau où le membre parasite se situe"))
                if 0 <= d < len(activ_fleet._spaceships):
                    choosed_spaceship = activ_fleet._spaceships[d]
                    if len(choosed_spaceship) == 0:
                        print("L'équipahe est vide")
                    else:
                        for i, member_ in enumerate(choosed_spaceship._crew, 1):
                            print(f"[{i}] {member_._first_name} {member_._last_name}")
                        member_index = int(input("Quel est le numéro du membre à supprimer ?")) - 1
                        if 0 <= deleted_member < len(choosed_spaceship._crew):
                            deleted_member = choosed_spaceship._crew[member_index]
                            choosed_spaceship.remove_member(deleted_member)
                        else:
                            print("Numéro invalide")
                else:
                    print("Numéro invalide")
        case "6":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship._name}")
                index = input("Quel est le numéro du vaisseau à afficher ?") - 1
                if 0 <= index < len(activ_fleet._spaceships):
                    selected_spaceship = activ_fleet._spaceships[index]
                    selected_spaceship.display()
                else:
                    print("Numéro invalide")
        case "7":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship}")
                index = int(input("Quel est le numéro du vaisseau à vérifier ?"))
                if 0 <= index < len(activ_fleet._spaceships):
                    selected_spaceship = activ_fleet._spaceships[index]
                    selected_spaceship.check_preparation()
                else:
                    print("Numéro invalide")
        case "8":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship}")
                spaceship_index = int(input("Quel est le numéro du vaisseau où se situe le membre à vérifier ?"))
                if 0 <= spaceship_index < len(activ_fleet._spaceships):
                    selected_spaceship = activ_fleet._spaceships[spaceship_index]
                    if len(selected_spaceship._crew) == 0:
                        print("Ce vaisseau n'a aucun membre")
                    else:
                        for i, member in enumerate(selected_spaceship._crew, 1):
                            print (f"[{i}] {member}")
                        member_index = int(input("Quel est le numéro du membre à vérifier ?"))
                        if 0 <= member_index < len(selected_spaceship._crew):
                            selected_member = selected_spaceship._crew[member_index]
                            if hasattr(selected_member, 'act'):
                                selected_member.act()
                            else:
                                print(f"{selected_member} ne fait pas d'action")
                        else:
                            print("Numéro invalide")
                else:
                    print("Numéro invalide")
        case "9":
            break
