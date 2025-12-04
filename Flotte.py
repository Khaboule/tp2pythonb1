class Flotte:
    def __init__(self,first_name, last_name, gender, age, name, spaeceships):
        super().__init__(first_name, last_name, gender, age)
        self.__name = name
        self.__spaceships = []

    def append_spaceship(self, spaceships):
        

