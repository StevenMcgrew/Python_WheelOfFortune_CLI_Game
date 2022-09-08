from wheel import Wheel


class Player:
    def __init__(self, name, game_score=0, round_score=0, has_free_play=False):
        self.name = name
        self.game_score = game_score
        self.round_score = round_score
        self.has_free_play = has_free_play

    def spin_wheel(self):
        wheel = Wheel()
        return wheel.spin()
