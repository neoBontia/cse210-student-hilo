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

    def guess_card(self):
        self.guess = ""
        self.guess = input()
        return self.guess
