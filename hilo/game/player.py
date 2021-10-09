class Player:
    """A code template for a player of HiLo game. The responsibility of this 
      class of objects is to guess if the next card is higher or lower than the current card, 
      compare guess vs next card, update the dealer if the guess is correct or not,
      and determine whether or not it can play again.

      Attributes:
          guess (char): A character h/H or l/L.
      """

    def __init__(self):
        self.guess = ""
        self.play = ""
        self.is_correct = False

    def guess_card(self):
        self.guess = ""
        self.guess = input("Higher or lower? [h/l] ")

    def get_guess(self):
        return self.guess

    def want_to_play(self):
        self.play = input("Play again? [y/n] ")

    def get_play(self):
        return self.play

    """def check_answer(self):
        self.is_correct = False
        if (self.dealer.get_prev_card() < self.dealer.get_curr_card()):
            if(self.guess == 'h' or self.guess == 'H'):
                self.is_correct = True"""

    def update(self):
        return self.is_correct
