class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.stats = {
            "FGA": 0,
            "FGM": 0,
            "3PA": 0,
            "3PM": 0,
            "FTA": 0,
            "FTM": 0,
            "AS": 0,
            "RB": 0
        }

    @property
    def statistics(self):
        return self.stats

    def add_FG(self, result):
        self.stats["FGA"] += 1
        if result == "Scored":
            self.stats["FGM"] += 1

    def add_3P(self, result):
        self.stats["3PA"] += 1
        if result == "Scored":
            self.stats["3PM"] += 1

    def add_FT(self, result):
        self.stats["FTA"] += 1
        if result == "Scored":
            self.stats["FTM"] += 1

    def add_AS(self):
        self.stats["AS"] += 1

    def add_RB(self):
        self.stats["RB"] += 1


class Team:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.players = {}

    def add_player(self, name, number):
        self.players.append(Player(name, number))

    def get_player(self, number):
        return self.players.get(number)

    @property
    def players_list(self):
        return self.players.values()


class Match:
    def __init__(self):
        self.teams = {}

    def read_match_data_file(self, filename):
        with open(filename, 'r') as file:
            current_team = None
            for line in file:
                line = line.strip()
                if line.startswith("TEAM"):
                    _, team_name, team_abbreviation = line.split(" - ")
                    current_team = Team(team_name, team_abbreviation)
                    self.teams[team_abbreviation] = current_team
                elif line.startswith("#") and current_team is not None:
                    player_number, player_name = line[1:].split(" - ")
                    current_team.add_player(player_name, int(player_number))

    def get_team(self, abbreviation):
        return self.teams.get(abbreviation)

    def read_match_statistics_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")
                team_abbreviation = parts[0]
                player_number = int(parts[1][1:])
                stat_type = parts[2]
                team = self.get_team(team_abbreviation)
                if team is not None:
                    player = team.get_player(player_number)
                    if stat_type in ["FG", "3P", "FT"]:
                        result = parts[3]
                        if stat_type == "FG":
                            player.add_FG(result)
                        elif stat_type == "3P":
                            player.add_3P(result)
                        elif stat_type == "FT":
                            player.add_FT(result)
                    elif stat_type == "AS":
                        player.add_AS()
                    elif stat_type == "RB":
                        player.add_RB()

    def display_match(self):
        output = ""
        for team in self.teams.values():
            output += "-" * 84 + "\n"
            output += f"| {team.name:<78} |\n"
            output += "-" * 84 + "\n"
            output += "| Nbr | Name                         | FGA | FGM | 3PA | 3PM | FTA | FTM | AS | RB |\n"
            for player in team.players_list:
                stats = player.statistics
                output += f"| #{player.number:<3} | {player.name:<28} | {stats['FGA']:<3} | {stats['FGM']:<3} | {stats['3PA']:<3} | {stats['3PM']:<3} | {stats['FTA']:<3} | {stats['FTM']:<3} | {stats['AS']:<2} | {stats['RB']:<2} |\n"
            output += "-" * 84 + "\n"
        return output

    def write_match_details(self, filename):
        with open(filename, 'w') as file:
            file.write(self.display_match())

if __name__ == "__main__":
    match = Match()
    match.read_match_data_file("d:/School/P1 2/Examenopgaves/Basketball/match_data.txt")
    match.read_match_statistics_file("d:/School/P1 2/Examenopgaves/Basketball/match_statistics.txt")
    match.write_match_details("d:/School/P1 2/Examenopgaves/Basketball/output.txt")

def fix_statistics_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            corrected_line = line.replace("SCored", "Scored")
            file.write(corrected_line)

fix_statistics_file("d:/School/P1 2/Examenopgaves/Basketball/match_statistics.txt")