import random


class PuzzleData:

    puzzle = ''
    category = ''
    puzzle_state = ''
    amount_complete = 0
    puzzles = [
        {"category": "SHOW BIZ",
         "puzzle": "THEATER CURTAIN"},

        {"category": "EVENT",
         "puzzle": "STUNNING LAST-SECOND VICTORY"},

        {"category": "WHAT ARE YOU DOING?",
         "puzzle": "WALKING THE DOG"},

        {"category": "PHRASE",
         "puzzle": "THE PRESSURE IS ON"},

        {"category": "EVENT",
         "puzzle": "TOURING EUROPE"},

        {"category": "PERSON",
         "puzzle": "LEADING CONTENDER"},

        {"category": "SAME NAME",
         "puzzle": "POKER AND TORTILLA CHIPS"},

        {"category": "PLACE",
         "puzzle": "ONE-OF-A-KIND LOCATION"},

        {"category": "LIVING THING",
         "puzzle": "PINK DAFFODIL"},

        {"category": "PHRASE",
         "puzzle": "STANDING ROOM ONLY"},

        {"category": "EVENT",
         "puzzle": "STRIKING GOLD"},

        {"category": "ON THE MAP",
         "puzzle": "AMSTERDAM"},

        {"category": "PHRASE",
         "puzzle": "LET THE CURRENTS CARRY YOU"},

        {"category": "BEFORE AND AFTER",
         "puzzle": "SOCIAL BUTTERFLY COLLECTOR"},

        {"category": "FOOD AND DRINK",
         "puzzle": "THE BEST PRETZEL EVER"},

        {"category": "LIVING THING",
         "puzzle": "LABRADOR RETRIEVER"},

        {"category": "LIVING THING",
         "puzzle": "SAINT BERNARD"},

        {"category": "THING",
         "puzzle": "THE SPIRIT OF ADVENTURE"},

        {"category": "PERSON",
         "puzzle": "PRIME MINISTER"},

        {"category": "PHRASE",
         "puzzle": "I HAVE LOFTY AMBITIONS"},
    ]

    def set_random_puzzle(self):

        # Choose random puzzle by index
        last_index = len(self.puzzles) - 1
        random_puzzle_index = random.randint(0, last_index)
        puzzle_data = self.puzzles.pop(random_puzzle_index)

        # Set puzzle and category
        self.puzzle = puzzle_data['puzzle']
        self.category = puzzle_data['category']

    def update_puzzle_state(self, letters):

        new_puzzle_state = ''

        # Loop to set '*' for hidden letters
        for char in self.puzzle:

            # Set '-' as revealed
            if char == '-':
                new_puzzle_state += char
                continue

            # Set ' ' as two spaces instead of one, to make the spaces more visible when printed
            if char == ' ':
                new_puzzle_state += '  '
                continue

            # If used letter, set as revealed
            if char in letters.used_vowels or char in letters.used_consonants:
                new_puzzle_state += char
                continue

            # Hidden letter is set to '*'
            new_puzzle_state += '*'

        # Set puzzle_state
        self.puzzle_state = new_puzzle_state

    def update_amount_complete(self):

        # Calculate how much of the puzzle has been revealed
        length = len(self.puzzle_state)
        spaces = self.puzzle_state.count(' ')
        total = length - spaces
        blanks = self.puzzle_state.count('*')
        filled = total - blanks
        completion_amt = filled / total

        # Set it
        self.amount_complete = completion_amt

    def has_vowels_remaining(self, letters):
        # This is needed to notify players when no more vowels remain in the puzzle
        return any(item in self.puzzle for item in letters.vowels)

    def has_consonants_remaining(self, letters):
        # This is needed to notify players when no more consonants remain in the puzzle
        return any(item in self.puzzle for item in letters.consonants)
