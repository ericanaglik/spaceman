import random
import string



possible_letters = list(string.ascii_lowercase)
#guess = int('')

# template load word
def load_word(): # works
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    return secret_word

def get_blank_word(secret_word, letters_guessed):  #letters_guessed is a list of the letters i guessed.
    # String that stores blanks if letter is incorrect or blanks and correct letter if guess is correct
    hidden_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            hidden_word += letter + ""
        else:
            hidden_word += " _ "
    return hidden_word

def choices_available(letters_guessed):
    choices = list("abcdefghijklmnopqrstuvwxyz")
    for letter in letters_guessed:
        if letter in choices:
            # remive that letter in choices
            choices.remove(letter)
        else:
            print("Please guess a single letter or a letter not guessed before")
    return choices

def is_secret_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True







"""
# create user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input
"""

# multiply blanks by the length of secret word


# increments through each letter in the secret word. if the letter is equal to the user's guess, the blank at the index becomes the guess
# if the letter is equal to the guess, letter found is true, otherwise, if it is false and the guess is appended to the guessed letters array





def spaceman():




"""
helper functions:




 later developments:
  - 7 lives
  - ascii
  - stretch: give the user after winning a choice to restart without turning off the terminal
  - stretch: secret word phrase to give user option to guess full word.



"""
