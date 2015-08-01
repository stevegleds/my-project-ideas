# Global Variables
teams_in_group = 6

# Initialise

team1 = "Ukraine"
team2 = "Poland"
team3 = "England"
team4 = "Moldova"
team5 = "Montenegro"
team6 = "San Marino"
team_group_a = set([])  # create empty set to store teams


def init():
    for i in range(teams_in_group):  # create first group by creating objects of class Team from team list
        name = eval("team" + str(i + 1))  # converts string to variable name
        a_team = Team(name)  # create team with name - name
        team_group_a.add(a_team)  # add a_team to team group


def find_element(search,
                 content):  # returns the first element in content that contains the element to be found - search
    # this can then be used to work out the result of the matches and build the table
    return [element for element in content if element[0] == search or element[2] == search]


def get_fixtures():
    with open('fixtures.txt') as fixturesfile:
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


def process_results(resultssofar) -> object:  # using this to see if I can add goals up. so far only works on first result
    total_goals = 0
    print("results so far: ", resultssofar)
    for match_result in resultssofar:
        print(match_result)
        print(match_result[1], " versus ", match_result[3] )
        total_goals += int(match_result[1]) + int(match_result[3])
        print("goals so far: ", total_goals)
    return


# Define classes
class Team:
    def __init__(self, name):
        self.name = name
        return

    def get_name(self):
        return self.name


# class Result:
#     def __init__(self, name):
#         self.name = name
#         return

# Let's get started
init()
fixtures = get_fixtures()
results = clean_up(fixtures)
print("Fixtures before results are split is called: ", fixtures)
results = split_matches(results, 3)
print("These are the results so far ", results)
process_results(results)