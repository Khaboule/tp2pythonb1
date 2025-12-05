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
        else:
            return
        if len(self.__spaceships) < 15:
            self.__spaceships.append(new_spaceship)
        else:
            print(f"La flotte {self.__name} contient déjà 15 vaisseaux.")

    
    def statistics(self):
        total_member = 0
        role_repartition = {}
        operators_experience_average = 0

        for Vaisseau in self._spaceships:
            for Member in Spaceship._crew:
                total_member += 1
                if isinstance(Member, Operator):
                    role = Member._role
                    operators_experience_average += Member._experience
                else:
                    role = "Membre de base"
                    

        
