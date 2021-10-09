import random
from game.player import Player

class Dealer:
    """
    This class is the dealer or the director of the HiLo game.
    This class is responsible for generating and displaying the cards
    that the player will guess, and is also responsible for calculating
    the points of the player based on his guess.

    Attributes:
    prev_card (number): the value of the previous card ranging from 1-13.
    curr_card (number): the value of the current card ranging from 1-13.
    points (points): the current points of the player. Initializes at 300.
    player (Player): an instance of Player.
    """

    def __init__(self):
        """
        This method initializes Dealer and its attributes.

        Attributes:
        self (Dealer): an instance of Dealer.
        """
        self.prev_card = random.randint(1, 13)
        self.curr_card = 0
        self.points = 300
        self.player = Player()
        self.can_play = True

    def display_card(self):
        """
        This method assigns a value for the current card and displays the value
        of the previous card.

        Attribute:
        self (Dealer): an instance of Dealer.
        """
        self.curr_card = random.randint(1, 13)

        print(f"The card is: {self.prev_card}")

    def check_answer(self):
        if (self.prev_card < self.curr_card):
            if(self.player.get_guess() == 'h' or self.player.get_guess() == 'H'):
                return True
            else:
                return False
        elif self.prev_card > self.curr_card:
            if self.player.get_guess() == 'L' or self.player.get_guess() == 'l':
                return True
            else:
                return False

    def calculate(self):
        """
        This method calculates the points of the player based on the result of
        their guess. Assigns the value of curr_card to prev_card to prepare for another
        round of HiLo.

        Attribute:
        self (Dealer): an instance of Dealer.
        """
        if self.check_answer():
            self.points += 100
            print(f"Your score is: {self.points}")
        else:
            self.points -= 75
            print(f"Your score is: {self.points}")

        self.prev_card = self.curr_card

    def get_prev_card(self):
        """
        This method returns the value of the prev_card.

        Attribute:
        self (Dealer): an instance of Dealer.
        """
        return self.prev_card

    def get_curr_card(self):
        """
        This method returns the value of the curr_card.

        Attribute:
        self (Dealer): an instance of Dealer.
        """
        return self.curr_card

    def will_play(self):
        if self.points <= 0:
            self.can_play = False
        if self.player.get_play() == "N" or self.player.get_play() == "n":
            self.can_play = False

    def play(self):
        """
        This method calls the appropriate methods to play the game while the player
        can still play.

        Attribute:
        self (Dealer): an instance of Dealer.
        """
        while self.can_play:
            self.display_card()
            self.player.guess_card()
            print(f"Current card: {self.curr_card}")
            self.calculate()
            if self.points > 0:
                self.player.want_to_play()
            self.will_play()
