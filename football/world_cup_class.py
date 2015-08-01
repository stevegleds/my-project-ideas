# Global Variables
def get_group_teams(resultssofar, group_teams):
    team_list = []
    print( "in get teams function", resultssofar)
    for match_result in resultssofar:  # to update the team objects with info from the results
        print("I am processing this result", match_result)
        print("team is: ", match_result[0])
        if match_result[0] not in team_list:  # need to create a team
            print(team_list)
            print("adding ", match_result[0])
            team_list.append(match_result[0])
            print("added: ", match_result[0] )
            print(team_list)            
        if match_result[2] not in team_list:
            print(team_list)
            print("adding ", match_result[2])
            team_list.append(match_result[2])
            print("added: ", match_result[2])
            print(team_list)
    print("final team list is: ******", team_list)
    return team_list

def find_element(search,
                 content):  # returns the first element in content that contains the element to be found - search
    # this can then be used to work out the result of the matches and build the table
    return [element for element in content if element[0] == search or element[2] == search]


def get_fixtures():
    with open("football/fixtures.txt") as fixturesfile:
        fixtureslist = fixturesfile.read().split()
    print(fixtureslist)
    return fixtureslist


def clean_up(fixtures_messy):
    # remove half time scores
    for entry in fixtures_messy:
        if '(' in entry:
            assert isinstance(entry, object)
            fixtures_messy.remove(entry)
    return fixtures_messy


def split_matches(fixtures_blob, n):  # split into individual matches - split into list of elements of n strings
    # I expect n to be 3
    if n < 1:
        n = 1
    fixtures_split = [fixtures_blob[i:i + n] for i in range(0, len(fixtures_blob), n)]
    for result in fixtures_split:  # takes each result and replaces "0:1" with '0' and adds '1' to end of list
        if str(result[1]) == "-":
            pass
        else:
            home_goals = result[1][0]  # temp store
            away_goals = result[1][2]  # temp store
            result[1] = home_goals  # replace "0:1" with '0'
            result.append(away_goals)  # adds '1' to end of list

    return fixtures_split


def process_results(
        resultssofar, group_teams) -> object:  # using this to see if I can add goals up.
    total_goals = 0
    print("results so far: ", resultssofar)
    for match_result in resultssofar:
        print(match_result[0], " versus ", match_result[2])
        # print(eval(group_teams[England]))
        hometeam = group_teams[(match_result[0])]  # hometeam now points to the home team object
        print("home team is: ", hometeam.name)
        print("hometeam scored : ", hometeam.name, " ", hometeam.scored)
        hometeam.scored += int(match_result[1])
        print("hometeam have now scored : ", hometeam.scored)
        awayteam = group_teams[(match_result[2])]  # hometeam now points to the home team object
        print("away team is: ", awayteam.name)
        print("awayteam scored : ", awayteam.scored)
        awayteam.scored += int(match_result[3])
        print("away team have now scored : ", awayteam.name, " ", awayteam.scored)
        total_goals += int(match_result[1]) + int(match_result[3])
        print("goals so far: ", total_goals)
    return


# Define classes
class Team:
    def __init__(self, name):
        self.name = name
        self.scored = 0
        self.against = 0
        self.points = 0
        self.opposition = []
        return

    def get_name(self):
        return self.name

    def get_for(self):
        return self.scored

    def get_against(self):
        return self.against

    def get_points(self):
        return self.points

    def process_result(self, opposition, scored, against):
        self.opposition.append([opposition, scored, against])
        self.scored += scored
        self.against += against
        if scored == against:
            self.points += 1
        elif scored > against:
            self.points += 3
        print("Result, for, against, points", str(self.opposition), self.scored, self.against, self.points)


def create_team(new_team_name, group_teams):
    new_team = Team(new_team_name)  # create Team object called new_team_name
    print(new_team.name)
    group_teams[new_team.name] = new_team  # Add the new_team object to the group_teams dic
    return group_teams

# Let's get started
group_teams = {}  # create dic to store team objects
#  create_team("blank team")

fixtures = get_fixtures()
results = clean_up(fixtures)
print("Here are the Fixtures before results are split is called: ", fixtures)
results = split_matches(results, 3)
print("These are the results so far ", results)
group_teams_list = get_group_teams(results, group_teams)

process_results(results, group_teams) # error: team is being created twice - overwriting previous creation and resetting goals etc.
print("this is the teams dic: ", group_teams)
'''
21 September 2014 created get_group_teams function. removed .lower() now get unique teams in list.
Need to use this team list to create team objects
'''
# 10 October 2014 Need to create teams from teams list in get-teams
