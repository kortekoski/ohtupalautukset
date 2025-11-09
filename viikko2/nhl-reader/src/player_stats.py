from rich.table import Table
from rich.console import Console

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = []

    def set_players(self, season):
        self.players = self.reader.get_players(season)

    def get_all_nationalities(self):
        nationalities = set()

        for player in self.players:
            nationalities.add(player.get_nationality())

        return nationalities
    
    def sort_players(self, players):
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            players,
            reverse=True,
            key=sort_by_points
        )

        return sorted_players
    
    def top_scorers_by_nationality(self, nationality):
        listed_players = []

        for player in self.players:
            if player.get_nationality() == nationality:
                listed_players.append(player)

        sorted_players = self.sort_players(listed_players)
        
        return sorted_players
    
    def print_table(self, players, nationality):
        table = Table(title=f"Top scorers ({nationality})")

        table.add_column("Player", style="cyan", no_wrap=True)
        table.add_column("Teams", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console = Console()
        console.print(table)