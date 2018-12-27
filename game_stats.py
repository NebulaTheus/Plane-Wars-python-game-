class GameStats():
    def __init__(self,ai_set):
        self.ai_set=ai_set
        self.reset_start()
        self.game_active=False
    def reset_start(self):
        self.ships_left=self.ai_set.ship_limit
        self.score=0

