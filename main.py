import random
import string
from man import man_dict  # getting the visuals of hangman from man file
from words import words  # getting words from words file

def hangman():  # creating hangman function
    word = random.choice(words)  # getting random word from word list
    w_letters = set(word)
    alphabet = set(string.ascii_lowercase)  # getting lowercase alphabet
    guessed = set()

    lives: int = 7  # setting number of lives

    # user input
    while len(w_letters) > 0 and lives > 0:
        print("You have", lives, "lives left. :0")
        print("You have guessed the letters: ", " ".join(guessed))

        # list of letters in word, letter replaced with "-" when not guessed yet
        word_list = [letter if letter in guessed else '-' for letter in word]
        print(man_dict[lives])
        print("Word: ", " ".join(word_list))
        print()

        user_letter = input("Please guess a letter: ").lower()
        if user_letter in alphabet - guessed:  # when letter from input is in alphabet, that has not been guessed yet
            guessed.add(user_letter)
            if user_letter in w_letters:
                w_letters.remove(user_letter)
                print("You found a letter!")

            else:
                lives = lives - 1
                print("This letter is not in the word. :(")

        elif user_letter in guessed:
            print("That letter has already been guessed. Please guess a new one.")
        else:
            print("Please guess a letter:")

    if lives == 0:  # when lives run out
        print(man_dict[lives])
        print("Oh no! You died. The word was:", word)
    else:
        print("Yay, you got it! The word was:", word + '!')


answer = input('Play game? (y/n) ')

while answer != 'n':
    if __name__ == '__main__':
        hangman()
    answer = input("Play again? (y/n) ")

print("Thanks for playing! :D")