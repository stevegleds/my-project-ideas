# Global Variables
teams_in_group = 6

# Initialise

team1="Ukraine"
team2="Poland"
team3="England"
team4="Moldova"
team5="Montenegro"
team6="Poland"
team_group_a = set([]) #create empty set to store teams

def init():
    for i in range(teams_in_group): #create first group
        name = eval("team"+str(i+1)) #converts string to variable name
        a_team = Team(name) #create team with name - name
        team_group_a.add(a_team) # add a_team to team group
    
	
        

#Define s
class Team:
    def __init__(self, name):
        self.name = name
        return

    def get_name(self):
        return self.name

#
# Let's get started
competition = str(input("What competition is this? " ))
init() 
print(competition)
for team in team_group_a:
            print(team.get_name())

###************ Define Variables ************
##
#
##
##teamA="Ireland"
##teamB="Spain"
##teamC="Croatia"
##teamD="Italy"
##
###Define Game Results
##
###Home Team, Home Goals, Away Team, Away Goals
##
##game1 = (teamA,0,teamB,4)
##game2 = (teamA,1,teamC,3)
##game3 = (teamA,0,teamD,2)
##game4 = (teamB,1,teamC,0)
##game5 = (teamB,1,teamD,1)
##game6 = (teamC,1,teamD,1)
##
###Define Points etc - Stats
##
###Points, For, Against, Difference
##
##teamAstats = [0,0,0,0]
##teamBstats = [0,0,0,0]
##teamCstats = [0,0,0,0]
##teamDstats = [0,0,0,0]
##
###************ Procedures and Functions ************
##
### whichGame takes the gameID from the loop integer and changes it to the corresponding game variable e.g. game1
##
##def whichGame(gameID):
##    if gameID==1:
##        return game1       
##    elif gameID==2:
##        return game2
##    elif gameID==3:
##        return game3
##    elif gameID==4:
##        return game4        
##    elif gameID==5:
##        return game5        
##    else:
##        return game6
##
### whichTeamStats takes the real name from teamID and changes it to the corresponding stats variable e.g. teamAstats
##
##def whichTeamStats(teamID):
##    if teamID=="Ireland":
##        return teamAstats
##    elif teamID=="Spain":
##        return teamBstats
##    elif teamID=="Croatia":
##        return teamCstats
##    else: return teamDstats
##
### procssResult takes the game number (1 to 6) and first prints the result then calls the updateStats procedure
##
##def processResult(game):
##    game=whichGame(game)
##    #print "************************************"
##    print "This Game was between",game[0],"and",game[2]
##    if game[1]>game[3]:
##        print game[0],"won",game[1],"-",game[3]
##        gameResult="win"
##        updateStats(gameResult,game[0],game[1],game[2],game[3])
##    elif game[3]>game[1]:
##        print game[2],"won",game[3],"-",game[1]
##        gameResult="win"
##        updateStats(gameResult,game[2],game[3],game[0],game[1])
##    else:
##        print game[0],"and",game[2],"drew",game[1],"all"
##        gameResult="draw"
##        updateStats(gameResult,game[0],game[1],game[2],game[3])
##    print "************",game
##    
### updateStats takes the info from processResult to update the stats for the teams involved
##
##def updateStats(result,winner,winningGoals,loser,losingGoals):
##    if result=="draw":
##        print "draw"
##        stats=whichTeamStats(winner)
##        print "The first team Stats were:",stats
##        stats[0]=stats[0]+1
##        stats[1]=stats[1]+winningGoals
##        stats[2]=stats[2]+losingGoals
##        stats[3]=stats[3]+winningGoals-losingGoals
##        print "The first team stats are now:",stats
##        stats=whichTeamStats(loser)
##        print "The second team Stats were:",stats
##        stats[0]=stats[0]+1
##        stats[1]=stats[1]+losingGoals
##        stats[2]=stats[2]+winningGoals
##        stats[3]=stats[3]+losingGoals-winningGoals
##        print "The second team stats are now:",stats
##        return
##    else:
##        stats=whichTeamStats(winner)
##        print "The winner Stats were:",stats
##        stats[0]=stats[0]+3
##        stats[1]=stats[1]+winningGoals
##        stats[2]=stats[2]+losingGoals
##        stats[3]=stats[3]+winningGoals-losingGoals
##        print "The winner stats are now:",stats
##        stats=whichTeamStats(loser)
##        print "The loser Stats were:",stats
##        stats[0]=stats[0]+0
##        stats[1]=stats[1]+losingGoals
##        stats[2]=stats[2]+winningGoals
##        stats[3]=stats[3]+losingGoals-winningGoals
##        print "The loser stats are now:",stats
##        return
    
#************************ This is the MAIN program ************

#print the current table for comparison
    
##print "TABLE"
##print "Team, Points,For,Against,Difference"
##print teamA, teamAstats
##print teamB, teamBstats
##print teamC, teamCstats
##print teamD, teamDstats
##
###this loops through all the results to process the result and update the stats. Not sure why 1 to 7 and not 1 to 6!
##
##for i in range(1,7):
##    print processResult(i)
##
###print the Final standings
##    
##print "FINAL TABLE"
##print "Team, Points,For,Against,Difference"
##print teamA, teamAstats
##print teamB, teamBstats
##print teamC, teamCstats
##print teamD, teamDstats


