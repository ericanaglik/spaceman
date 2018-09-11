import random
import string

# control d breaks it

secret_word = ''
word_letter_list = []
guessed_letters = []
possible_letters = list(string.ascii_lowercase)
hidden_letters = list("_" * len(secret_word))


def load_word():
    global secret_word

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    print(secret_word)

def create_blanks(secret_word):
    count = 0
    for letter in secret_word:
        print("_", end= "")
        count += 1
    print("There are {} letters in the chosen word".format(count))

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def gen_hidden_letters():
    global secret_word
    global hidden_letters

def letter_replaced(secret_word):
    global guessed_letters
    print("guesed letters: {}".format(guessed_letters))
    shown_letters = list(secret_word)
    print("shown letters: {}".format(shown_letters))
    for i, item in enumerate(shown_letters):
        for letters in guessed_letters:
            print(i)
            print("hidden letters {}".format(hidden_letters))
            if shown_letters[i] == letters:
                hidden_letters[i] = letters
    return (hidden_letters, shown_letters)

def spaceman(secret_word):
    print("The secret word is: " + secret_word)
    #print("There are " + len(secret_word) + "letters in the secret word.")
    create_blanks(secret_word)
    guesses = 0
    while guesses != 7:
        input_letter = user_input("Please guess a letter: ")
        print("Input letter: {}".format(input_letter))
        if input_letter in possible_letters:
            guessed_letters.append(input_letter)
            if input_letter in secret_word:
                letter_replaced(secret_word)
            else:
                print(guessed_letters)
                guesses += 1
        elif input_letter in guessed_letters:
            print("Please enter a letter not guessed before")
        else:
            print("Please enter a single letter")

load_word()
spaceman(secret_word)
