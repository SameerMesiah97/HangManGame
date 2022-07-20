import random

class Game:
    def __init__(self):
        self.lives = 6
        self.words = list(line.strip() for line in open('words.txt'))
        self.game_end = False
        self.game_won = False

    def select_word(self):
        return self.words[random.randint(0, len(self.words) -1)]

    def convert_word (self,word):
        letters = []
        for letter in word:
            letters.append([letter, False])
        return letters


class Display:
    def show_hangman (self, lives):

        hangmen = ["    +---+\n" + "        |\n" + "        |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "        |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "    |   |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "  / |   |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "  / | \ |\n" + "        |\n",
                   "    +---+\n" + "    O   |\n" + "  / | \ |\n" + "   /    |\n",
                   "    +---+\n" + "    O   |\n" + "  / | \ |\n" + "   / \  |\n"]

        print (hangmen[len(hangmen)-lives-1])

    def show_letters (self, letters):


        for letter in letters:
            if letter[1] == True:
                print(letter[0].upper(), end=' ')
            else:
                print ("_",end=' ')
        print ("\n")

    def show_lives(self, lives):

        print (f"You have {lives} lives left!")