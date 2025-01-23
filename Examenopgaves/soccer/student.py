class Team:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.games_drawn = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.goal_difference = 0
        self.points = 0

    def play(self, opponent, goals_for, goals_against):
        self.games_played += 1
        self.goals_scored += goals_for
        self.goals_conceded += goals_against
        self.goal_difference = self.goals_scored - self.goals_conceded

        opponent.games_played += 1
        opponent.goals_scored += goals_against
        opponent.goals_conceded += goals_for
        opponent.goal_difference = opponent.goals_scored - opponent.goals_conceded

        if goals_for > goals_against:
            self.games_won += 1
            self.points += 3
            opponent.games_lost += 1
        elif goals_for < goals_against:
            self.games_lost += 1
            opponent.games_won += 1
            opponent.points += 3
        else:
            self.games_drawn += 1
            self.points += 1
            opponent.games_drawn += 1
            opponent.points += 1

class Competition:
    def __init__(self):
        self.teams = {}

    def add_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)

    def get_team(self, team_name):
        return self.teams.get(team_name)

    def update_competition(self, match_results):
        for team_a, team_b, score_a, score_b in match_results:
            if team_a not in self.teams:
                self.add_team(team_a)
            if team_b not in self.teams:
                self.add_team(team_b)
            self.teams[team_a].play(self.teams[team_b], score_a, score_b)

    def display_table(self):
        table = "Team          | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts\n"
        for team in self.teams.values():
            table += f"{team.name:<14} | {team.games_played:<3} | {team.games_won:<3} | {team.games_drawn:<3} | {team.games_lost:<3} | {team.goals_scored:<4} | {team.goals_conceded:<4} | {team.goal_difference:<5} | {team.points:<3}\n"
        return table

    def write_table(self, filename):
        with open(filename, 'w') as file:
            file.write(self.display_table())

def read_match_data_file(filename):
    match_results = []
    with open(filename, 'r') as file:
        for line in file:
            team_a, rest = line.split(' - ')
            team_b, scores = rest.split(': ')
            score_a, score_b = map(int, scores.split(' - '))
            match_results.append((team_a, team_b, score_a, score_b))
    return match_results

def process_match_data(match_data_file_name, output_file_name):
    competition = Competition()
    match_results = read_match_data_file(match_data_file_name)
    competition.update_competition(match_results)
    competition.write_table(output_file_name)