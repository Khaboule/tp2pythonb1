from Member import *
class Mentaliste(Member):

    def __init__(self, first_name, last_name, gender, age, mana):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana

    @property
    def _mana(self):
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = value

    def act(self):
        self.mana = self.mana - 20

    def recharge_mana(self):
        if self.mana <= 50:
            self.mana = self.mana + 50
        else:
            self.mana = self.mana + (self.mana - 50)
