import random
import sys

class GuessingGame:
    low, high, guess, secretNumber = int, int, int, int

    def __init__(self):

        self.setLow()
        self.setHigh()
        self.setGuess()

        self.secretNumber = random.randint(self.low, self.high)

    def setLow(self):
        low = int(input("I'm thinking about a number between: "))
        self.low = low

    def setHigh(self):
        high = int(input("and: "))
        self.high = high

    def setGuess(self):
        guess = int(input("Please type a number: "))
        self.guess = guess

    def playGame(self):
        while self.guess != self.secretNumber:
            print("Sorry wrong number")
            if self.guess > self.secretNumber:
                print("Try a little lower")
            else:
                print("Try a little higher")
            self.setGuess()
        print(f"That is correct! {self.guess} was the number I was thinking of!")
        sys.exit()
    def tryGuess(self):
        
        print(f"Is {self.guess} the number?\n")
        print("Press Y for yes and N for no\n")
        selection = input()
        while selection.upper() != 'Y':
            self.guess = random.randint(self.low, self.high)
            print("give me a hint, was I to low(L) or to high (H)")
            feedback = input("Please type L or H:  ")
            if feedback == 'L':
                self.low = self.guess + 1
                self.tryGuess()
            elif feedback == 'H':
                self.high = self.guess - 1
                self.tryGuess()
            else:
                print("That was not quite right lets try again")
        print(f"Awesome! So {self.guess} was the number you were thinking!")
        sys.exit()

    def computerPlays(self):
        self.tryGuess()

guessingGame = GuessingGame()
guessingGame.computerPlays()
    