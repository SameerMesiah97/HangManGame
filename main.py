import hangman

new_game = hangman.Game()
word = new_game.select_word()
letters = new_game.convert_word(word)
game_display = hangman.Display()

while new_game.game_end == False:

    game_display.show_hangman(new_game.lives)
    game_display.show_letters(letters)
    guess = input("Enter a letter:")

    correct_guess = False

    for letter in word:
        if guess.lower() == letter.lower():
            letters[word.index(letter)][1] = True
            print("Correct Guess")
            correct_guess = True
            break;

    if correct_guess == False:
        new_game.lives -= 1
        print("Wrong Guess")
        game_display.show_lives(new_game.lives)

    if new_game.lives == 0:
        game_display.show_hangman(0)
        new_game.game_end = True
        new_game.game_won = False

    count = 0

    for x in letters:
        if x[1] == False:
            continue
        else:
            count += 1

    if count == len (letters):
        new_game.game_end = True
        new_game.game_won = True

if new_game.game_won:
    print("You have won.")
else:
    print("You have lost.")