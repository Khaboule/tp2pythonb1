from Member import Member


class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience


#Getter et Setter        


    @property
    def _role(self):
        return self.__role

    @_role.setter
    def _role(self, value):
        self.__role = value

    @property
    def _experience(self):
        return self.__experience

    @_experience.setter
    def _experience(self, value):
        self.__experience = value


#Méthodes


    def act(self):
        if self.__role == "technicien":
            print( self.__first_name, "vérifie le moteur") 
        elif self.__role == "pilote":
            print( self.__first_name, "vérifie ses commandes")
