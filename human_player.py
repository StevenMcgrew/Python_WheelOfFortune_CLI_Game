from player import Player
from strings import INVALID_INPUT_WARNING
from colorama import Fore
yellow = Fore.YELLOW


class HumanPlayer(Player):

    def solve_puzzle(self):
        return input("\n  Type the answer to solve the word puzzle: ").upper()

    def choose_option(self, options):

        # This is used both for the intro and the regular game play options
        while True:
            choice = input(f"\n  {self.name}, please choose an option: ")

            # Validate choice
            if choice not in options:
                print(f"{yellow}{INVALID_INPUT_WARNING}")
                continue

            # Return choice
            return choice

    def guess_a_consonant(self, letters):
        while True:
            guess = input(
                "\n  Which consonant would you like to guess?: ").upper()

            # Validate consonant
            if guess not in letters.consonants:
                print(
                    f"    {yellow}That letter is not in the list of remaining consonants.")
                continue

            # Return consonant
            return guess

    def guess_a_vowel(self, letters):
        while True:
            guess = input("\n  Which vowel would you like to guess?: ").upper()

            # Validate vowel
            if guess not in letters.vowels:
                print(
                    f"    {yellow}That letter is not in the list of remaining vowels.")
                continue

            # Return vowel
            return guess
