from Member import Member
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet
import json
import ast

fleets = []
activ_fleet = None

#Création d'une flotte en la renommant via le input et en l'intégrant à la liste fleets et retourne la nouvelle flotte
def create_fleet():
    name_fleet = input("Quel est le nom de la nouvelle flotte ?")
    new_fleet = Fleet(name_fleet, [])
    fleets.append(new_fleet)
    print(f"Flotte '{name_fleet}' créée")
    return new_fleet

#Si la liste fleets est vide alors retourne aucune flotte sinon retourne toutes les flottes numérotées de 1 à n
def choose_fleet():
    if len(fleets) == 0:
        print("Aucune flotte n'existe")
        return
    print("Flotte(s) disponible(s)")
    for i, fleet in enumerate(fleets, 1):
        nb_spaceships = len(fleet._spaceships)
        print(f"{i} {fleet._name} {nb_spaceships}")
#Si le numéro de flotte choisie est valide renvoie la flotte sinon renvoie numéro invalide
    choice2 = int(input("\nQuelle flotte voulez vous sélectionner ?")) - 1
    if 0 <= choice2 < len(fleets):
        return fleets[choice2]
    else:
        print("Numéro invalide")
        return



#Sauvegarde des données via json on sauvegarde la flotte avec vaisseaux, membres, roles dedans
def save_data(fleet, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(fleet, file, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
    
    print(f"Flotte '{fleet._name}' sauvegardée dans {file_name}")


#On charge le fichier avec la flotte qu'on veut 
def load_data(file_name):
    import os
    print(f"Dossier actuel : {os.getcwd()}")
    print(f"Fichiers présents : {os.listdir('.')}")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        fleet = Fleet(data['_Fleet__name'], [])
        for spaceship_data in data['_Fleet__spaceships']:
            spaceship = Spaceship(
                spaceship_data['_Spaceship__name'],
                spaceship_data['_Spaceship__ship_type'],
                None,
                spaceship_data['_Spaceship__condition']
            )
            for member_data in spaceship_data['_Spaceship__crew']:
                if '_Operator__role' in member_data:
                    member = Operator(
                        member_data['_Member__first_name'],
                        member_data['_Member__last_name'],
                        member_data['_Member__gender'],
                        member_data['_Member__age'],
                        member_data['_Operator__role'],
                        member_data['_Operator__experience']
                    )
                elif '_Mentalist__mana' in member_data:
                    member = Mentalist(
                        member_data['_Member__first_name'],
                        member_data['_Member__last_name'],
                        member_data['_Member__gender'],
                        member_data['_Member__age'],
                        member_data['_Mentalist__mana']
                    )
                else:
                    member = Member(
                        member_data['_Member__first_name'],
                        member_data['_Member__last_name'],
                        member_data['_Member__gender'],
                        member_data['_Member__age']
                    )
                spaceship.append_member(member)
            fleet.append_spaceship(spaceship)
        print(f"Flotte '{fleet._name}' chargée depuis {file_name}")
        return fleet
    except FileNotFoundError:
        print(f"Fichier {file_name} introuvable")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None


#Boucle while true pour l'affichage avec 2 parties la premiere pour gérer les flottes et la 2eme pour gerer la flotte sélectionnée
#On accède à la 2eme partie que quand activ_fleet est valide dans quand on a une flotte de prête ça facilite l'utilisation et rend le visuel plus agréable
while True:
    print("--- Gestion des flottes ---")
    print("[A] Créer une nouvelle flotte")
    print("[B] Charger une flotte")
    print("[C] Supprimer une flotte")


#Présentation des commandes possibles sur la flotte choisie
    if activ_fleet:
        print("\n[1] Renommer la flotte")
        print("[2] Ajouter un vaisseau à la flotte")
        print("[3] Supprimer un vaisseau à la flotte")
        print("[4] Ajouter un membre d'équipage")
        print("[5] Supprimer un membre d'équipage")
        print("[6] Afficher les informations d'un équipage")
        print("[7] Vérifier la préparation d'un vaisseau")
        print("[8] Vérifier l'action d'un membre d'équipage")
        print("[9] Sauvegarder la flotte")
        print("[10] Afficher les statistiques")
    print("[0] Quitter\n")
    choice = input("Quel est votre choix ?")
    match choice:
        case "A":
            activ_fleet = create_fleet()
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
        case "B":
            file_name = input("Nom du fichier à charger (ajoutez bien le .json à la fin): ")
            loaded_fleet = load_data(file_name)
            if loaded_fleet:
                fleets.append(loaded_fleet)
                activ_fleet = loaded_fleet
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
                activ_fleet.append_spaceship(new_spaceship)
        case "3":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                for i, spaceship in enumerate(activ_fleet._spaceships, 1):
                    print (f"[{i}] {spaceship._name}")
                b = int(input("Choisissez le numéro du vaisseau à supprimer")) - 1
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
                c = int(input("Choisissez le numéro du vaisseau où le nouveau membre sera déployé")) - 1
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
                    age = int(input("Age:"))
                    if type_member == "1":
                        role = input("Choisissez le rôle (technicien/pilote/navigateur/médecin/ingénieur)")
                        new_member = Operator(first_name, last_name, sexe, age, role)
                    elif type_member == "2":
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
                d = int(input("Choisissez le numéro du vaisseau où le membre parasite se situe")) - 1
                if 0 <= d < len(activ_fleet._spaceships):
                    choosed_spaceship = activ_fleet._spaceships[d]
                    if len(choosed_spaceship._crew) == 0:
                        print("L'équipahe est vide")
                    else:
                        for i, member_ in enumerate(choosed_spaceship._crew, 1):
                            print(f"[{i}] {member_._first_name} {member_._last_name}")
                        member_index = int(input("Quel est le numéro du membre à supprimer ?")) - 1
                        if 0 <= member_index < len(choosed_spaceship._crew):
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
                index = int(input("Quel est le numéro du vaisseau à afficher ?")) - 1
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
                    print (f"[{i}] {spaceship._name}")
                index = int(input("Quel est le numéro du vaisseau à vérifier ?")) - 1
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
                    print (f"[{i}] {spaceship._name}")
                spaceship_index = int(input("Quel est le numéro du vaisseau où se situe le membre à vérifier ?")) - 1
                if 0 <= spaceship_index < len(activ_fleet._spaceships):
                    selected_spaceship = activ_fleet._spaceships[spaceship_index]
                    if len(selected_spaceship._crew) == 0:
                        print("Ce vaisseau n'a aucun membre")
                    else:
                        for i, member in enumerate(selected_spaceship._crew, 1):
                            print (f"[{i}] {member._first_name} {member._last_name}")
                        member_index = int(input("Quel est le numéro du membre à vérifier ?")) - 1
                        if 0 <= member_index < len(selected_spaceship._crew):
                            selected_member = selected_spaceship._crew[member_index]
                            if hasattr(selected_member, 'act'):
                                selected_member.act()
                            else:
                                print(f"{selected_member._first_name} ne fait pas d'action")
                        else:
                            print("Numéro invalide")
                else:
                    print("Numéro invalide")
        case "9":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                file_name = input("Nom du fichier de sauvegarde: ")
                if not file_name.endswith('.json'):
                    file_name += '.json'
                save_data(activ_fleet, file_name)
                
        case "10":
            if not activ_fleet:
                print("Aucune flotte n'est disponible")
            else:
                activ_fleet.statistics()
        case "0":
            break


#La grande majoritée du code dans l'affichage est une répétition des memes choses entre l'affichage des flottes, vaisseaux ou membres numérotées
#ainsi que la réaffectation de variable je ne pense pas que ce soit tres utile d'expliquer chaque point