class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def get_name(self) -> str:
        return self.name
    
    def get_score(self) -> int:
        return self.score
    
    def get_score_call(self) -> str:
        score_calls = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        
        return score_calls.get(self.score)
    
    def add_point(self) -> None:
        self.score += 1

    def has_winning_score(self) -> bool:
        return self.score >= 4