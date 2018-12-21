import sys
import os
import pprint
import math

class DraftProjectMain:
    class Player:
        def __init__(self):
            self.draftPosition = 0
            self.continent = ''
            self.gamesPlayed = 0
            self.gamesPlayedAboveAveragePercentage = 0.0
            
    def __init__(self):
        self.players = []
        self.naPlayers = 0.0
        self.naGpaap = 0.0
        self.euPlayers = 0.0
        self.euGpaap = 0.0
        
    def loadPlayers(self, year):
        fileName = '%d_Entry_Draft.csv' % year
        f = open(fileName)
        for line in f:
            p = self.Player()
            contents = line.split(',')
            p.draftPosition = int(contents[0])
            p.continent = contents[4]
            p.gamesPlayed = float(contents[5])
            self.players.append(p)
            
        for i in xrange(0, len(self.players)):
            self.calculateGpaap(i)
            
        
    def calculateGpaap(self, index):
        # print 'calculateGpaap'
        player = self.players[index]
        range = int(math.sqrt(player.draftPosition))
        range = max(range, 3)
        range = min(range, 11)
        
        gamesPlayed = 0.0
        playersCounted = 0
        
        for i in xrange(max(0, index-range-1), min(len(self.players), index+range+1)):
            gamesPlayed += self.players[i].gamesPlayed
            playersCounted += 1
            
        if gamesPlayed > 0:
            player.gamesPlayedAboveAveragePercentage = player.gamesPlayed/(gamesPlayed/playersCounted)

        
        if player.continent == 'NA':
            self.naPlayers += 1
            self.naGpaap += player.gamesPlayedAboveAveragePercentage
        else:
            self.euPlayers += 1
            self.euGpaap += player.gamesPlayedAboveAveragePercentage
        
        
def main():
    naPlayersTotal = 0
    naGpaapTotal = 0.0
    euPlayersTotal = 0
    euGpaapTotal = 0.0
    
    for year in xrange(2005, 2015):
        draftProject = DraftProjectMain()
        draftProject.loadPlayers(year)
        print '%d:' % year
        print 'North America Average GPAAP: %f' % (draftProject.naGpaap/draftProject.naPlayers)
        print 'Europe Average GPAAP: %f' % (draftProject.euGpaap/draftProject.euPlayers)
        naPlayersTotal += draftProject.naPlayers
        naGpaapTotal += draftProject.naGpaap
        euPlayersTotal += draftProject.euPlayers
        euGpaapTotal += draftProject.euGpaap
        
   
    print 'Total 2005-2014:'
    print 'North America Average GPAAP: %f' % (naGpaapTotal/naPlayersTotal)
    print 'Europe Average GPAAP: %f' % (euGpaapTotal/euPlayersTotal)

if __name__ == "__main__":
    main()
        