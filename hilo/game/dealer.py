import random
from game import Player

class Dealer:
    """
    This class is the dealer or the director of the HiLo game.
    This class is responsible for generating and displaying the cards
    that the player will guess, and is also responsible for calculating
    the points of the player based on his guess.
    """

    def __init__(self):
        self.prev_card = random.randint(1, 13)
        self.curr_card = 0
        self.points = 300
        self.player = Player()

    def display_card(self):
        self.curr_card = random.randint(1, 13)

        print(f"The card is: {self.prev_card}")

    def calculate(self):
        if self.player.update():
            self.points += 100
            print(f"Your score is: {self.points}")
        else:
            self.points -= 75
            print(f"Your score is: {self.points}")

        self.prev_card = self.curr_card

    def get_prev_card(self):
        return self.prev_card

    def get_curr_card(self):
        return self.curr_card

    """def play(self):
        while self.player.can_play:
            self.display_card()
            self.player.guess_card()
            self.player.check_answer()
            self.calculate()
            """
