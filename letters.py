class Letters:

    # Letters are removed as they are used, and placed into the 'used_...' lists
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                  'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    used_vowels = []
    used_consonants = []

    # List of consonants ordered by frequency of use in the english language. To be used by computer_player for guessing letters.
    consonants_by_freq = ['R', 'T', 'N', 'S', 'L', 'C', 'D', 'P',
                          'M', 'H', 'G', 'B', 'F', 'Y', 'W', 'K', 'V', 'X', 'Z', 'J', 'Q']

    def reset(self):

        # Put vowels and consonants back into their lists
        self.vowels = self.vowels + self.used_vowels
        self.consonants = self.consonants + self.used_consonants

        # Clear the used vowels and consonants lists
        self.used_vowels.clear()
        self.used_consonants.clear()

        # Sort the vowels and consonants in alphabetical order
        self.vowels.sort()
        self.consonants.sort()
