from Member import *
class Mentalist(Member):

    def __init__(self, first_name, last_name, gender, age, mana):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana


#Getter et Setter


    @property
    def _mana(self):
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = value


#Méthodes


    def act(self):
        self._mana = self._mana - 20

    def recharge_mana(self):
        if self._mana <= 50:
            self._mana = self._mana + 50
        else:
            self._mana = self._mana + (self._mana - 50)
