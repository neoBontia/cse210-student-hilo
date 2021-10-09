import random
from game import Player

class Dealer:

    def __init__(self):
        self.card = 0
        self.points = 300
        self.player = Player()

    def display_card(self):
        self.card = random.randint(1, 13)

        print(f"The card is: {self.card}")

    def calculate(self):
        if self.player.update():
            self.points += 100
            print(f"Your score is: {self.points}")
        else:
            self.points -= 75
            print(f"Your score is: {self.points}")

    """def play(self):
        while self.player.can_play:
            self.display_card()
            self.player.guess_card()
            self.player.check_answer()
            self.calculate()
            """