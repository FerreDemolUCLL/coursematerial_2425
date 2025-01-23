def make_teams(participants, team_size):
    team_count = len(participants)//team_size
    teams = list()
    while team_count > 0:
        team = list()
        team.append(participants[:team_size+1])
        del participants[:team_size+1]
        team_count -= 1
        teams.append(team)

    count = 0
    while len(participants) > 0:
        teams[count].append(participants[-1])
        count += 1
    
    return teams