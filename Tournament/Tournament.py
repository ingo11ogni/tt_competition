#!/usr/bin/python
import os
import config.Tournament_Config as tc


class Tournament(object):

    def __init__(self):
        self._date = None
        self._place = None
        self._event_name = None
        self._event_list = None
        self._match_manager = None
        self._player_manager = None
        self._registration_manager = None
        self._tournament_progress_manager = None
        self._results_manager = None
        self._resource_manager = None

    def read_tournament_details(self):
        pass

    def read_event_types(self):
        file = open(tc.event_type_path, "r")
        lines = file.readlines()
        file.close()

        print "events %s" % lines

    def read_player_lists(self):
        pass

    def read_partnerships(self):
        pass


if __name__ == '__main__':
    print "Tournament..."
    tournament = Tournament()
    tournament.read_event_types()
    print "Done!"
