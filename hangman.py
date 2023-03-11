# 3/10/2023 Dallin Jackson Hangman Game for OIT interview
# Start Time: 19:15   End Time: 23:07
import random

print("\nWelcome to Hangman! :)")

# gets player_name
name = input("\nLet's get started! What's your name?: ")
instructions = "In Hangman, a random word is selected and it is your job to guess what it is. A list of blank spaces" \
               "\nwill be shown like this:" \
               "\n _ _ _ _ _" \
               "\nwhich would mean your word has five letters in it. It's also important to know you can guess whole" \
               "\nwords! But each letter in the word you guess will be counted as a separate guess. If you guess a " \
               "\nletter you have already guessed, you'll be asked to guess again. Don't worry, we'll keep track of" \
               "\nthe letters you guess. Be careful of the wrong guesses, it's not called \'Hangman\' for nothing." \
               "\nIf you're down to play, enter your name and start guessing some letters!"

print("Hi " + name + "! " + instructions)

# Sees if user wants to play a round
farewell = "Thanks for playing " + name + "! Have a great day"


def wants_to_play(again="a"):
    wants = input("Would you like to play " + again + " round? Enter (y/n): ").lower()
    if wants != "y" and wants != "n":
        wants = input("Sorry we didn't get your input, please use a y or an n key. \nWould you like to "
                      "play " + again + " round? Enter (y/n): ").lower()
    if wants == "y":
        return True
    elif wants == "n":
        print(farewell)
        return False


def print_gallows(oops):
    if oops % 6 == 1:
        print("_________"
              "\n |	|"
              "\n	|"
              "\n	|"
              "\n	|"
              "\n	|"
              "\n_____|||||||")
    elif oops % 6 == 2:
        print("_________"
              "\n |	|"
              "\n 0	|"
              "\n	|"
              "\n	|"
              "\n	|"
              "\n_____|||||||")
    elif oops % 6 == 3:
        print("_________"
              "\n |	|"
              "\n 0	|"
              "\n/|	|"
              "\n	|"
              "\n	|"
              "\n_____|||||||")
    elif oops % 6 == 4:
        print("_________"
              "\n |	|"
              "\n 0	|"
              "\n/|\     |"
              "\n	|"
              "\n	|"
              "\n_____|||||||")
    elif oops % 6 == 5:
        print("_________"
              "\n |	|"
              "\n 0	|"
              "\n/|\     |"
              "\n /	|"
              "\n	|"
              "\n_____|||||||")
    elif oops % 6 == 0 and oops != 0:
        print("_________"
              "\n |	|"
              "\n 0	|"
              "\n/|\     |"
              "\n /\	|"
              "\n	|"
              "\n_____|||||||")
    if oops > 24:
        print("Hung: 4")
    elif oops > 18:
        print("Hung: 3")
    elif oops > 12:
        print("Hung: 2")
    elif oops > 6:
        print("Hung: 1")


# function for playing a word
def turn(word_list, already, blanks_list, correct_score, oops_score, correctly_guessed):
    print("\nLetters to Guess: ", *blanks_list)  # player can see what is left to guess
    guess_input = input("Enter a guess: ")
    guess = [i for i in guess_input]

    for i in guess:
        if i in already:
            print("You've already guessed \"" + i + "\" but we won't hold that against you.")
            return turn(word_list, already, blanks_list, correct_score, oops_score, correctly_guessed)

    for char in guess:
        if char not in word_list:
            oops_score += 1
        for i in range(len(word_list)):
            if word_list[i] == char:
                blanks_list[i] = word_list[i]
                correct_score += 1
        already.append(char)

    if "_" not in blanks_list:
        correctly_guessed = True
        print("\nCorrect Guesses: " + str(correct_score) + "\nIncorrect Guesses: " + str(oops_score) + " ")
        print("Letters Already Guessed: ", *already)
        print("Congratulations! You guessed the word \"" + word_list + "\" with " + str(oops_score) + " wrong guesses!")
        print_gallows(oops_score)
        return correctly_guessed
    else:

        print("\nCorrect Guesses: " + str(correct_score) + "\nIncorrect Guesses: " + str(oops_score) + " ")
        print("Letters Already Guessed: ", *already)
        print_gallows(oops_score)
        return turn(word_list, already, blanks_list, correct_score, oops_score, correctly_guessed)


# words to be used in the game
ten_words = ["pineapple", "carbonation", "stork", "frequency", "victorious", "brilliant", "oquirrh", "laptop",
             "boulder", name.lower()]
rounds_played = 0

# sees if user wants to start playing
play = None
while play is None:
    play = wants_to_play()

while play and rounds_played <= 9:
    """setting up round"""
    word = ten_words.pop(random.randrange(len(ten_words)))
    blanks = ["_" for _ in range(len(word))]
    turn(word, [], blanks, 0, 0, False)
    rounds_played += 1
    # sees if user wants to play again
    play = None
    while play is None:
        play = wants_to_play("another")
if rounds_played > 9:
    print("Thank you so much for your enthusiasm to keep playing! That's all we have for you today, have a great day "
          + name + "!")
