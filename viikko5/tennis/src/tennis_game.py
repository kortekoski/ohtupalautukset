from entities.player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player1.add_point()
        elif player_name == self.player2.get_name():
            self.player2.add_point()

    def define_draw(self):
        current_score = self.player1.get_score()

        draw_calls = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }

        return draw_calls.get(current_score, "Deuce")
        
    def is_score_drawn(self):
        return self.player1.get_score() == self.player2.get_score()
    
    def player_has_winning_score(self):
        return self.player1.has_winning_score() or self.player2.has_winning_score()
    
    def advantage_to_string(self, player, advantage):
        if advantage == 1:
            return f"Advantage {player.get_name()}"
        if advantage >= 2:
            return f"Win for {player.get_name()}"
        return "Deuce"
    def define_win_or_deuce(self):
        player1_advantage = self.player1.get_score() - self.player2.get_score()

        if player1_advantage > 0:
            return self.advantage_to_string(self.player1, player1_advantage)
        else:
            return self.advantage_to_string(self.player2, abs(player1_advantage))
        
    def get_score_call(self):
        return f"{self.player1.get_score_call()}-{self.player2.get_score_call()}"

    def get_score(self):
        if self.is_score_drawn():
            return self.define_draw()
        
        if self.player_has_winning_score():
            return self.define_win_or_deuce()

        return self.get_score_call()
