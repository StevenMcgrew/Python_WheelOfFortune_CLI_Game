import random


class Wheel:

    wheel_prizes = ("BANKRUPT", 5000, 500, 900, 700, 300, 800, 550, 400, 500, 600, 350,
                    500, 900, "BANKRUPT", 650, 1000, 700, "LOSE A TURN", 800, 500, 450, 500, 300)

    def spin(self):
        return random.choice(self.wheel_prizes)
