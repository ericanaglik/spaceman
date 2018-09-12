import random
import string

blanks = []
guessed_letters = []
possible_letters = list(string.ascii_lowercase)
guess = int('')

# template load word
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    return secret_word

# create user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# multiply blanks by the length of secret word
def create_blanks():
    global secret_word
    global blanks
    blanks = list(' - ' * len(secret_word))

# increments through each letter in the secret word. if the letter is equal to the user's guess, the blank at the index becomes the guess
# if the letter is equal to the guess, letter found is true, otherwise, if it is false and the guess is appended to the guessed letters array
def replace_letter(guess):
    global secret_word
    global blanks
    global letter_found
    letter_found = False
    count = 0
    for letter in secret_word:
        if letter == guess:
            letter_found = True
            blanks[count] = guess
        count += 1
    if not letter_found:
        guessed_letters.append(guess)

# converts the list blanks and guessed letters into strings to be printed to the console
def display():
    global blanks
    global guess
    guess = 0
    string_blanks = ""
    string_guessed_letters = "Guessed letters: "
    for i in blanks:
        string_blanks = string_blanks + i
    print(string_blanks)

    for i in guessed_letters:
        string_guessed_letters = string_guessed_letters + i + ' '
    print(string_guessed_letters)
    guess += 1


def spaceman():
    running = True
    while running:
        global secret_word
        load_word()
        input_letter = user_input("Please guess a letter: ")
        if input_letter in possible_letters:
            replace_letter(input_letter)
            display()
        else:
            print("Please enter a single letter")

def test():
    create_blanks()
    replace_letter("m")
    replace_letter("x")
    replace_letter("p")
    display()
    print(secret_word)
    print(blanks)

test()
