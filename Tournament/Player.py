
class Player(object):

    def __init__(self, name, surname, grade="TBA"):
        self._name = name
        self._surname = surname
        self._grade = grade
        self._events = None
        self._partner = None
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @surname.deleter
    def surname(self):
        del self._surname

