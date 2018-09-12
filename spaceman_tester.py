import random
import string

# control d breaks it


def load_word():
    # opens the file and reads it.
    f = open('words.txt', 'r
    # 
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    return secret_word

def create_blanks():
    global secret_word
    global blanks
    blanks = list('_' * len(secret_word))

def user_input(prompt):
    user_input = input(prompt)
    return user_input

# def gen_hidden_letters():
#     global secret_word
#     global hidden_letters

def replace_letter(guess):
    global secret_word
    global blanks
    count = 0
    for i in secret_word:
        if i == guess:
            blanks[count] = guess
        count += 1

def spaceman(secret_word):
    print("The secret word is: " + secret_word)
    #print("There are " + len(secret_word) + "letters in the secret word.")
    create_blanks()
    guesses = 0
    while guesses != 7:
        input_letter = user_input("Please guess a letter: ")
        if input_letter in possible_letters:
            guessed_letters.append(input_letter)
            replace_letter(input_letter)
        else:
            print(guessed_letters)
            guesses += 1
        elif input_letter in guessed_letters:
            print("Please enter a letter not guessed before")
        else:
            print("Please enter a single letter")

load_word()
spaceman(secret_word)




"""
helper functions:

we need to produce a word to guess

hide word from user
    - with underscores _ _ _ _

user guesses a letter
    - if the letter is in the word replaces the underscore of the correct letter locationself.
    - if not in the word

choices_available
 - removes once the user guesses a letter
 - stores it a list of guessed letters
 - guessed_letters list of choices input

is_secret_word_guessed
 - this is how you win...


 later developments:
  - 7 lives
  - ascii
  - stretch: give the user after winning a choice to restart without turning off the terminal
  - stretch: secret word phrase to give user option to guess full word.



"""
