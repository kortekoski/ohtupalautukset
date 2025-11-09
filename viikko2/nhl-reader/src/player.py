class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.points = self.goals + self.assists
    
    def get_nationality(self):
        return self.nationality

    def __str__(self):
        return str(f"{self.name:<20} {self.team:<20} points {self.goals} + {self.assists} = {self.points:>5}")
