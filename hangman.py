import random


class Game:
    # Load list of words from text document.
    words = list(line.strip() for line in open('words.txt'))

    def get_word_from_list(self):

        # Random word is selected from the list.
        word = self.words[random.randint(0, len(self.words) - 1)]

        letters = []

        # Word is converted into a list of lists representing letters that have been guessed/not guessed.
        for letter in word:
            letters.append([letter, False])
        return letters

    def __init__(self):
        self.__lives_left = 6
        self.__game_letters = self.get_word_from_list()
        self.__game_state = {"ended": False, "won": False}

    def get_lives(self):
        return self.__lives_left

    def set_lives(self, lives_left):
        self.__lives_left = lives_left

    def get_game_letters(self):
        return self.__game_letters

    def set_game_letters(self, letters):
        self.__game_letters = letters

    def get_game_state(self):
        return self.__game_state

    def set_game_state(self, state):
        self.__game_state = state

    def win(self):
        for letter in self.get_game_letters():
            # If at least one letter has not been correctly guessed, game has not been won
            if not letter[1]:
                return False
        return True

    def correct_guess(self, guess):
        for letter in self.get_game_letters():
            if guess.lower() == letter[0].lower():
                return True
        return False

    def has_game_ended(self):

        # Game ends when no lives remain or all letters have been guessed correctly.
        if self.get_lives() == 0:
            return True
        if self.win():
            return True
        return False

    def play_game(self):

        print ("Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters.\n"
               "If too many letters which do not appear in the word are guessed, the player is hanged (and loses).\n"
               "In this version of the game, you are allowed 6 incorrect guesses before you lose. \n")

        game_display = Display()

        while not self.__game_state["ended"]:

            lives = self.get_lives()
            letters = self.get_game_letters()

            print(game_display.get_hangman(lives))
            print(game_display.get_letters(letters))

            guess = input("Enter a letter:")

            if self.correct_guess(guess):
                for letter in letters:
                    if guess.lower() == letter[0].lower():
                        letter[1] = True

                print("Correct Guess")
            else:
                self.set_lives(lives - 1)
                lives = self.get_lives()

                print("Wrong Guess")

                if lives == 1:
                    print("You have 1 life left")
                else:
                    print(f"You have {lives} live(s) left!")

            # Determine if game has ended.
            if self.has_game_ended():

                # And if it has ended, determine if player has won or lost.
                if self.win():
                    print(game_display.get_letters(letters))
                    print("You have won.")
                    self.set_game_state({"ended": True, "won": True})
                else:
                    print(game_display.get_hangman(lives))
                    print("You have lost.")
                    self.set_game_state({"ended": True, "won": False})


class Display:
    def get_hangman(self, lives):

        hangmen = ["    +---+\n" + "        |\n" + "        |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "        |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "    |   |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "  / |   |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "  / | \ |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "  / | \ |\n" + "   /    |\n",
                   "    +---+\n" + "    O   |\n" + "  / | \ |\n" + "   / \  |\n"]

        return hangmen[len(hangmen) - lives - 1]

    def get_letters(self, letters):
        letters_string = ""

        for letter in letters:
            if letter[1]:
                letters_string += letter[0].upper()
            else:
                letters_string += "_"

        return letters_string
