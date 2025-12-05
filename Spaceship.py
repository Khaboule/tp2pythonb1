from Member import Member
from Operator import Operator

class Spaceship:
    def __init__(self, name, ship_type, crew=None, condition="Prêt"):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = crew if crew else []
        self.__condition = condition


#Getter et Setter


    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _ship_type(self):
        return self.__ship_type

    @_ship_type.setter
    def _ship_type(self, value):
        self.__ship_type = value

    @property
    def _crew(self):
        return self.__crew

    @_crew.setter
    def _crew(self, value):
        self.__crew = value

    @property
    def _condition(self):
        return self.__condition

    @_condition.setter
    def _condition(self, value):
        self.__condition = value


#Méthodes
        

    def append_member(self, new_member):
        if not isinstance(new_member, Member): # Vérifier que l'objet ajouté est un membre
            print("L'objet que vous essayez d'ajouter n'est pas un objet membre")
            return
        if len(self.__crew) < 10:
            self.__crew.append(new_member)
            print("Le membre a bien été ajouté au vaisseau")
        else:
            print("L'équipage est déjà rempli (max 10)")


        

    def check_preparation(self):
        has_pilote = False
        has_technician = False
        if len(self.__crew) < 2:
            print("L'equipage n'est pas pret pour la mission")
        else:
            for member in self.__crew:
                if member._role == "pilote":
                    has_pilot = True
                elif member._role == "technicien":
                    has_technician = True
        if has_pilot and has_technician:
            print("L'equipage est pret pour la mission")
        else:
            print("L'equipage n'est pas pret pour la mission")

        

    def remove_member(self, member):
        if not isinstance(member, Member):
            print("L'objet que vous essayez de retirer n'est pas un membre")
            return
    
        if member in self.__crew:
            self.__crew.remove(member)
            print(f"Le membre {member._first_name} {member._last_name} a été retiré du vaisseau")
        else:
            print("Ce membre ne fait pas partie de l'équipage")


    def display(self):
        if len(self.__crew) <= 0:
            print("L'equipage est vide")
        else:
            count = 1
            for member in self.__crew:
                print(f"- Membre : {str(count)} ")
                print(f"- Prénom : {member._first_name}")
                print(f"- Nom : {member._last_name}")
                print(f"- Genre : {member._gender}")
                print(f"- Age : {member._age}")
                if isinstance(member, Operator):
                    print(f"- Role : {member._role}")
                    print(f"- Expérience: {member._experience}")
                else:
                    print(f"- Rôle : Membre de base")
                print("---------------------------------")
                count += 1