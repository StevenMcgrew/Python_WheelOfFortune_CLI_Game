import sys
from strings import *
from gameboard_functions import build_gameboard
from colorama import Fore
yellow = Fore.YELLOW


class Game:

    def __init__(self, players, letters, puzzle_data):
        self.players = players
        self.active_player = players[0]
        self.round = 0
        self.is_intro_done = False
        self.letters = letters
        self.puzzle_data = puzzle_data

    def intro(self):
        print(yellow + TITLE + Fore.RESET + INTRO_OPTIONS)

        choice = self.active_player.choose_option(('1', '2', '3'))

        if choice == '1':
            self.start_new_round()
            return

        if choice == '2':
            print(GAME_INSTRUCTIONS)
            input("\n  Press ENTER to continue")
            self.intro()
            return

        if choice == '3':
            sys.exit(f"{yellow}{GOODBYE_MESSAGE}")

    def start_new_round(self):
        self.round += 1
        self.puzzle_data.set_random_puzzle()
        self.present_gameboard_and_options()

    def present_gameboard_and_options(self):
        self.print_game_board()
        print(GAMEPLAY_OPTIONS)
        self.present_gameplay_options()

    def print_game_board(self):

        # After the intro, halt game play in-between gameboard printing so screen doesn't scroll too far
        if self.is_intro_done:
            input("\n  Press ENTER to continue")

        self.puzzle_data.update_puzzle_state(self.letters)
        self.puzzle_data.update_amount_complete()
        print(build_gameboard(self.puzzle_data,
                              self.players,
                              self.letters,
                              self.round))

        # Set this flag so the program knows whether or not to halt game play in-between gameboard printing
        self.is_intro_done = True

    def present_gameplay_options(self):

        # Go to solving the puzzle if all of the letters of the puzzle have been filled in
        if '*' not in self.puzzle_data.puzzle_state:
            print(
                f"    {yellow}All the letters have been filled in.")
            self.player_attempts_solve()
            return

        # Get choice based on which player
        choice = ''
        if self.active_player.name == 'Game_Bot':
            choice = self.active_player.choose_option({'puzzle_data': self.puzzle_data,
                                                       'letters': self.letters})
        else:
            choice = self.active_player.choose_option(('1', '2', '3', '4'))

        if choice == '1':
            self.player_spins_wheel()
            return

        if choice == '2':
            self.player_buys_vowel()
            return

        if choice == '3':
            self.player_attempts_solve()
            return

        if choice == '4':
            self.exit_safely()

    def player_spins_wheel(self):

        # Check if any consonants remain in puzzle
        if not self.puzzle_data.has_consonants_remaining(self.letters):
            print(
                f"    {yellow}There are no more consonants in the puzzle. Please choose another option.")
            self.present_gameplay_options()
            return

        result = self.active_player.spin_wheel()
        self.print_wheel_spin_result(result)

        if result == "LOSE A TURN":
            self.next_players_turn()
            return

        if result == "BANKRUPT":
            self.active_player.round_score = 0
            self.next_players_turn()
            return

        # if result == "FREE PLAY":
        #     TODO: implement free play logic
        #     return

        # Wheel landed on a dollar amount
        self.player_guesses_consonant(result)

    def player_guesses_consonant(self, wheel_prize):

        consonant = self.active_player.guess_a_consonant(self.letters)

        # Remove letter from 'consonants' and append it to 'used_consonants'
        self.letters.used_consonants.append(
            self.letters.consonants.pop(self.letters.consonants.index(consonant)))

        # Check for letter in puzzle
        count = self.puzzle_data.puzzle.count(consonant)
        self.print_num_matches(consonant, count)

        if count == 0:
            self.next_players_turn()
        else:
            self.award_wheel_prize(wheel_prize, count)
            self.present_gameboard_and_options()

    def next_players_turn(self):
        self.set_next_player()
        print(f"    {yellow}It's {self.active_player.name}'s turn next.")
        self.present_gameboard_and_options()

    def player_buys_vowel(self):

        # Check if any vowels remain in puzzle
        if not self.puzzle_data.has_vowels_remaining(self.letters):
            print(
                f"    {yellow}There are no more vowels in the puzzle. Please choose another option.")
            self.present_gameplay_options()
            return

        # Check if player has enough money to buy a vowel
        if self.active_player.round_score < 250:
            print(
                f"    {yellow}Sorry, you don't have enough money to buy a vowel.")
            self.present_gameplay_options()
            return

        # Deduct money and proceed
        self.active_player.round_score -= 250
        self.player_guesses_vowel()

    def player_guesses_vowel(self):

        vowel = self.active_player.guess_a_vowel(self.letters)

        # Remove vowel from 'vowels' and append it to 'used_vowels'
        self.letters.used_vowels.append(
            self.letters.vowels.pop(self.letters.vowels.index(vowel)))

        # Check for vowel in puzzle
        count = self.puzzle_data.puzzle.count(vowel)
        self.print_num_matches(vowel, count)

        if count == 0:
            self.next_players_turn()
        else:
            self.present_gameboard_and_options()

    def player_attempts_solve(self):

        answer = ''

        # Get answer based on which player
        if self.active_player.name == 'Game_Bot':
            answer = self.active_player.solve_puzzle(self.puzzle_data)
        else:
            answer = self.active_player.solve_puzzle()

        # Check answer
        if answer == self.puzzle_data.puzzle:
            self.on_solve_success()
        else:
            self.on_solve_failure()

    def set_next_player(self):
        index_of_active_player = self.players.index(self.active_player)
        last_index = len(self.players) - 1

        if index_of_active_player == last_index:
            self.active_player = self.players[0]
        else:
            self.active_player = self.players[index_of_active_player + 1]

    def on_solve_success(self):

        # Print congratulations message
        print(
            f"    {yellow}Congratulations {self.active_player.name}! You solved the puzzle!")
        print(
            f"    {yellow}The correct answer is:  {Fore.RESET}{self.puzzle_data.puzzle}")

        # Add winner's money for this round to their game total, and reset all player's round_score to 0
        for player in self.players:
            if player.name == self.active_player.name:
                player.game_score += player.round_score
            player.round_score = 0

        if self.round == 3:
            # TODO: implement a bonus round
            self.end_of_game()
        else:
            # Reset the letters
            self.letters.reset()

            # Set the next player
            self.set_next_player()

            # Print message about next round
            next_round_phrase = 'the final round.'
            if self.round == 1:
                next_round_phrase = 'round 2.'
            print(
                f"    {yellow}{self.active_player.name} goes next in {next_round_phrase}")

            # Start the next round
            self.start_new_round()

    def on_solve_failure(self):
        print(f"    {yellow}Sorry, that is not the correct answer.")
        self.next_players_turn()

    def award_wheel_prize(self, prize, count):
        self.active_player.round_score += (prize * count)
        print(
            f"    {yellow}{self.active_player.name} wins ${prize} x {count} = ${prize * count}")

    def print_num_matches(self, letter, count):

        # Determine the correct verbage
        verbage = f"are {count} '{letter}'s"
        if count == 1:
            verbage = f"is {count} '{letter}'"
        if count == 0:
            verbage = f"are no '{letter}'s"

        # Print the message
        print(f"    {yellow}There {verbage} in the puzzle.")

    def print_wheel_spin_result(self, result):

        # Determine correct string for wheel spin result
        result_str = result
        if isinstance(result, int):
            result_str = f"${result}"

        # Print the message
        print(
            f"    {yellow}{self.active_player.name} spun the wheel and landed on {result_str}")

    def end_of_game(self):

        winner_name = ''
        winner_total = 0

        # Determine winner
        for player in self.players:
            if player.game_score > winner_total:
                winner_name = player.name
                winner_total = player.game_score

        # Print the winner and their total
        print(
            f"    {yellow}{winner_name} wins the game with a total of ${winner_total}")

        # End the game
        input("\n  Press ENTER to exit the game")

    def exit_safely(self):

        # Make sure the player didn't accidentally choose exit
        while True:
            answer = input(
                "\n  Are you sure you want to exit the game? (y/n) ").lower()

            if answer == 'y':
                sys.exit(f"{yellow}{GOODBYE_MESSAGE}")

            if answer == 'n':
                self.present_gameplay_options()
                break

            print(f"    {yellow}Please enter y for yes or n for no.")
