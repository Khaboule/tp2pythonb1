from Member import Member

class Spaceship:
    def __init__(self, name, ship_type, crew, condition):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = []
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
        else:
            return
        if len(self.__crew) < 10:
            self.__crew.append(new_member)
        else:
            print("L'équipage est déjà rempli (max 10)")


        

    def check_preparation(crew):
        has_pilote = False
        has_technician = False
        if len(crew) < 2:
            print("L'equipage n'est pas pret pour la mission")
        else:
            for member in crew:
                if member["role"] == "pilote":
                    has_pilot = True
                elif member["role"] == "technicien":
                    has_technician = True
        if has_pilot and has_technician:
            print("L'equipage est pret pour la mission")
        else:
            print("L'equipage n'est pas pret pour la mission")


