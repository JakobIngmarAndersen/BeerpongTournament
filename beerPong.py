from random import seed
from random import randrange
import time

'''
Program for random team-matchups for a beerpong tournament (2019)
'''

def gamesFrom4(teams):
    team1 = teams[randrange(len(teams))]
    teams.remove(team1)

    team2 = teams [randrange(len(teams))]
    teams.remove(team2)
    print(team1 + " vs. " + team2)

    team3 = teams[randrange(len(teams))]
    teams.remove(team3)

    team4 = teams[randrange(len(teams))]
    teams.remove(team4)
    print(team3  + " vs. " + team4)

def gamesFromRandomTeams(teams):
    while (len(teams) != 0 and len(teams)%2 != 1):
        team1 = teams[randrange(len(teams))]
        teams.remove(team1)
        team2 = teams[randrange(len(teams))]
        teams.remove(team2)
        print(team1 + " vs. " + team2)


teams = ["Jake og Eivind", "Thomas og Are", "Jdog og Martin", "Andreas og Jonas"]

seed(time.time())


#gamesFrom4(teams)
gamesFromRandomTeams(teams)