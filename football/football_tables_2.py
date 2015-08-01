#Define Variables
#Define Teams
teamA="Ireland"
teamB="Spain"
teamC="Croatia"
teamD="Italy"
#Define Game Results
#Home Team, Home Goals, Away Team, Away Goals
game1 = (teamA,0,teamB,4)
game2 = (teamA,1,teamC,3)
game3 = (teamA,0,teamD,2)
game4 = (teamB,1,teamC,0)
game5 = (teamB,1,teamD,1)
game6 = (teamC,1,teamD,1)

#Define Points etc
#Points, For, Against, Difference
teamAstats = [0,0,0,0]
teamBstats = [0,0,0,0]
teamCstats = [0,0,0,0]
teamDstats = [0,0,0,0]

def whichGame(game):
    if game==1:
        return game1       
    elif game==2:
        return game2
    elif game==3:
        return game3
    elif game==4:
        return game4        
    elif game==5:
        return game5        
    else:
        return game6
def whichTeamStats(teamID):
	if teamID=="Ireland":
		return teamAstats
	elif teamID=="Spain":
		return teamBstats
	elif teamID=="Croatia":
		return teamCstats
	else: return teamDstats
def processResult(game):
	game=whichGame(game)
	print "************************"
	print "This Game was between ",game[0], "and",game[2]
	if game[1]>game[3]:
		print game[0],"won",game[1],"-",game[3]
		gameResult="win"
		updateStats(gameResult,game[0],game[1],game[2],game[3])
	elif game[3]>game[1]:
		print game[2],"won",game[3],"-",game[1]
		gameResult="win"
		updateStats(gameResult,game[2],game[3],game[0],game[1])
	else:
		print game[0],"and",game[2],"drew",game[1],"all"
		gameResult="draw"
		updateStats(gameResult,game[0],game[1],game[2],game[3])
	print "************************", game
	
def updateStats(result,winner,winningGoals,loser,losingGoals):
	if result=="draw":
		stats=whichTeamStats(winner)
		stats[0]=stats[0]+1
		stats[1]=stats[1]+winningGoals
		stats[2]=stats[2]+losingGoals
		stats[3]=stats[3]+winningGoals-losingGoals
		stats=whichTeamStats(loser)
		stats[0]=stats[0]+1
		stats[1]=stats[1]+losingGoals
		stats[2]=stats[2]+winningGoals
		stats[3]=stats[3]-winningGoals+losingGoals
		return
	else:
		stats=whichTeamStats(winner)
		stats[0]=stats[0]+3
		stats[1]=stats[1]+winningGoals
		stats[2]=stats[2]+losingGoals
		stats[3]=stats[3]+winningGoals-losingGoals
		stats=whichTeamStats(loser)
		stats[0]=stats[0]+0
		stats[1]=stats[1]+losingGoals
		stats[2]=stats[2]+winningGoals
		stats[3]=stats[3]-winningGoals+losingGoals
		return
print "************ INITIAL TABLE ************"
print "Team, Points, For, Against, Goal Difference"
print teamA, teamAstats
print teamB, teamBstats
print teamC, teamCstats
print teamD, teamDstats

for i in range(1,7):
	processResult(i)
print "FINAL TABLE"
print "Team, Points, For, Against, Goal Difference"
print teamA, teamAstats
print teamB, teamBstats
print teamC, teamCstats
print teamD, teamDstats
