from Member import Member
from Operator import Operator
from Spaceship import Spaceship


class Fleet:

    def __init__(self, name, spaceeships):
        self.__name = name
        self.__spaceships = []


    # Getter et Setter


    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _spaceships(self):
        return self.__spaceships

    @_spaceships.setter
    def _spaceships(self, value):
        self.__spaceships = value


    # Méthodes


    def append_spaceship(self, new_spaceship):
        if not isinstance(new_spaceship, Spaceship): # Vérifier que l'objet ajouté est un vaisseau
            print("L'objet que vous essayez d'ajouter n'est pas un vaisseau")
            return
        if len(self.__spaceships) < 15:
            self.__spaceships.append(new_spaceship)
            print("Le vaisseau a bien été ajouté")
        else:
            print(f"La flotte {self.__name} contient déjà 15 vaisseaux.")

    
    def statistics(self):

        total_member = 0
        role_repartition = {}
        operators_experience_average = 0
        operator_count = 0

        for spaceship in self._spaceships:
            for member in spaceship._crew:

                total_member += 1

                if isinstance(member, Operator):
                    role = member._role
                    operators_experience_average += member._experience
                    operator_count += 1

                else:
                    role = "Membre de base"

                    role_repartition[role] = role_repartition.get(role, 0) + 1

        xp = (operators_experience_average/operator_count)
        print(f"\nNombre total de membre : {total_member}")
        print(f"\nRépartition des roles")
        for role, count in role_repartition.items():
            print(f"- {role} {count}")
        print(f"\nExperience des opérateurs: {xp}")

        
