class Match(object):

    def __init__(self):
        self._event_type = None
        self._player_1 = None
        self._player_2 = None
        self._progress_score = None
        self._result = None
        pass

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    @event_type.deleter
    def event_type(self):
        del self._event_type

    @property
    def player_1(self):
        return self._player_1

    @player_1.setter
    def player_1(self, value):
        self._player_1 = value

    @player_1.deleter
    def player_1(self):
        del self._player_1

    @property
    def player_2(self):
        return self._player_2

    @player_2.setter
    def player_2(self, value):
        self._player_2 = value

    @player_2.deleter
    def player_2(self):
        del self._player_2

    @property
    def progress_score(self):
        return self._progress_score

    @progress_score.setter
    def progress_score(self, value):
        self._progress_score = value

    @progress_score.deleter
    def progress_score(self):
        del self._progress_score

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @result.deleter
    def result(self):
        del self._result

