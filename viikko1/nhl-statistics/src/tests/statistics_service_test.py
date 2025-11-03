import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class StatisticsServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = StatisticsService(PlayerReaderStub())

    def test_search_existing_player(self):
        player = self.service.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_search_non_existing_player(self):
        player = self.service.search("Selänne")
        self.assertIsNone(player)

    def test_team_players(self):
        team_players = self.service.team("EDM")
        self.assertEqual(len(team_players), 3)
        for player in team_players:
            self.assertEqual(player.team, "EDM")

    def test_top_scorers(self):
        top_players = self.service.top(5)
        for player in top_players: print(player)
        print(top_players)
        self.assertEqual(len(top_players), 5)
        for i in range(4):
            self.assertGreaterEqual(top_players[i].points, top_players[i + 1].points)

    def test_top_goalers(self):
        top_goalers = self.service.top(5, SortBy.GOALS)
        self.assertEqual(len(top_goalers), 5)
        for i in range(4):
            self.assertGreaterEqual(top_goalers[i].goals, top_goalers[i + 1].goals)

    def test_top_assisters(self):
        top_assisters = self.service.top(5, SortBy.ASSISTS)
        self.assertEqual(len(top_assisters), 5)
        for i in range(4):
            self.assertGreaterEqual

    def test_top_scorers_with_sortby(self):
        top_players = self.service.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        expected_names = ["Gretzky", "Lemieux", "Yzerman"]
        for i in range(3):
            self.assertEqual(top_players[i].name, expected_names[i])