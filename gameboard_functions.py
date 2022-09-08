from colorama import Fore
blue = Fore.BLUE
reset = Fore.RESET


def build_round_scores(players, round):

    # Start off the string with the round
    scores_str = f"\n           {blue}Round{reset}:  {round}/3\n"

    # Add to it the players, scores for this round, and freeplay
    for player in players:
        scores_str += f"        {blue}{player.name}{reset}:  ${player.round_score}\n"
        if player.has_free_play:
            scores_str += f" FREEPLAY"

    return scores_str + "\n"


def build_remaining_letters(letters, puzzle_data):

    # Determine vowels_str based on vowels remaining in puzzzle
    vowels_str = ''
    if puzzle_data.has_vowels_remaining(letters):
        vowels_str = ' '.join(letters.vowels)
    else:
        vowels_str = "There are no more vowels in the puzzle"

    # Determine consonants_str based on consonants remaining in puzzle
    consonants_str = ''
    if puzzle_data.has_consonants_remaining(letters):
        consonants_str = ' '.join(letters.consonants)
    else:
        consonants_str = "There are no more consonants in the puzzle"

    # Finish building the 'remaining letters' string
    letters_str = f"          {blue}Vowels{reset}:  {vowels_str}\n"
    letters_str += f"      {blue}Consonants{reset}:  {consonants_str}\n"

    return letters_str


def build_puzzle_and_category(puzzle_data):
    return f"\n        {blue}Category{reset}:  {puzzle_data.category}\n          {blue}Puzzle{reset}:  {puzzle_data.puzzle_state}"


def build_game_scores(players):

    scores_str = '\n'

    # Concatenate the players and their total scores for the game thus far
    for player in players:
        scores_str += f"  {blue}{player.name} total{reset}:  ${player.game_score}\n"

    return scores_str


def build_gameboard(puzzle_data, players, letters, round):
    gameboard = build_game_scores(players)
    gameboard += build_round_scores(players, round)
    gameboard += build_remaining_letters(letters, puzzle_data)
    gameboard += build_puzzle_and_category(puzzle_data)
    return gameboard
