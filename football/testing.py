__author__ = 'Steve'
team = ['test']
results = [['england', 0, 'poland', 2], ['wales', 0, 'poland', 2], ['scotland', 0, 'wales', 2]]
for result in results:
    print("match", result[0], result[2])
    if result[0] not in team:
        team.append(result[0])
        print(result[0], team[0])
        print(team)
    if result[2] not in team:
        team.append(result[2])
        print(team)
    else:
        pass

print(team)



