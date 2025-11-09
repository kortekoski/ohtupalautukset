import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_seasons(self):
        response = requests.get(self.url)

        # read the root page as text and get the string containing available seasons
        seasons_text = response.text.split('available ')[1].split('<')[0]

        # split string by comma

        seasons = seasons_text.split(',')

        trimmed = [x.strip() for x in seasons]

        return trimmed

    def get_players(self, season):
        season_url = f'{self.url}{season}/players'
        response = requests.get(season_url).json()

        players = []

        for player_json in response:
            player = Player(player_json)
            players.append(player)

        return players