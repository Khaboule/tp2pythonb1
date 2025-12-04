class Vaisseau:
    def __init__(self,first_name, last_name, gender, age, name, ship_type, crew, condition):
        super().__init__(first_name, last_name, gender, age)
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = []
        self.__condition = condition

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
        
    def append_member(self, new_member):
        self.__crew.append(new_member)



        

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


