class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']
        self.points = self.goals + self.assists

    def get_nationality(self):
        return self.nationality

    def __str__(self):
        return str(f"{self.name:<20} {self.team:<20} points {self.goals} + {self.assists} = {self.points:>5}")
