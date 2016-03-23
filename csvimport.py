#                           #
#                           #
#  READING FROM A .CSV FILE #
#                           #
#                           #

## Turn .csv import file into a class

import csv as csv
import player
import unicodedata

class DKSalaryImport:

    def __init__(self, filename):
        with open(filename, 'rb') as dksalaries:
            dksalariesreader = csv.reader(dksalaries, delimiter=',')
            startrow = 7
            currentrow = 0
            self.players = {}
            for row in dksalariesreader:
                if currentrow > startrow:
                    playerobject = player.Player(row[11], row[13], int(row[14]), int(row[15]), row[16], row[17])
                    self.players[playerobject.name] = playerobject
                currentrow += 1

    def PlayerList(self):
        return self.players


