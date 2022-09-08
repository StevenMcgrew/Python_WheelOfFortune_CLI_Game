import random
from player import Player
from colorama import Fore
yellow = Fore.YELLOW


class ComputerPlayer(Player):

    def __init__(self, name="Game_Bot", game_score=0, round_score=0, has_free_play=False):
        super().__init__(name, game_score, round_score, has_free_play)
        self.choice_dict = {
            '1': 'spin the wheel',
            '2': 'buy a vowel',
            '3': 'solve the puzzle'
        }

    def choose_option(self, dic):
        print(f"\n  {self.name} please choose an option:")

        # First, default to choosing option 1) Spin the wheel
        choice = '1'

        # If no more consonants, change to option 3) Solve the puzzle
        if not dic['puzzle_data'].has_consonants_remaining(dic['letters']):
            choice = '3'

        # If puzzle 70% complete or more, change to option 3) Solve the puzzle
        if dic['puzzle_data'].amount_complete >= 0.7:
            choice = '3'

        print(
            f"    {yellow}{self.name} chooses to {self.choice_dict[choice]}.")
        return choice

    def solve_puzzle(self, puzzle_data):
        # Game_Bot submits the puzzle (the correct answer) when it is ready to solve
        return puzzle_data.puzzle

    def guess_a_consonant(self, letters):

        guess = ''

        # Of the remaining consonants, find the most frequently used in the English language
        for char in letters.consonants_by_freq:
            if char in letters.consonants:
                guess = char
                break

        print(f"    {yellow}{self.name} guesses letter '{guess}'.")
        return guess

    def guess_a_vowel(self, letters):
        # Use random guess for vowel
        guess = random.choice(letters.vowels)
        print(f"    {yellow}{self.name} guesses letter '{guess}'.")
        return guess
