from colorama import init
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from letters import Letters
from puzzle_data import PuzzleData
from game import Game


def main():

    # Initialize colorama
    init(autoreset=True)

    # Initialize game
    human = HumanPlayer('Player_1')
    computer = ComputerPlayer()
    letters = Letters()
    puzzle_data = PuzzleData()
    game = Game((human, computer),
                letters,
                puzzle_data)

    # Start the game
    game.intro()


if __name__ == '__main__':
    main()
