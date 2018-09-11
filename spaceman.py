import random


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    print(secret_word)
    return secret_word9

def updateLetters():
    shown_letters = list(secretWord)
    hidden_letters = list("_" * len(shown_letters))
    for i, item in enumerate(shown_letters):
        for letters in guessed_letters:
            if shown_letters[i] == letters:
                hidden_letters[i] = letters
    return (hidden_letters, shown_letters)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess. This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of the secretWord are in lettersGuessed;
    False otherwise
    '''
    secretWord = load_word()
    lettersGuessed = list()

    if secretWord.find(lettersGuessed):
        return True
    else:
        return False




# def get_guessed_word(secret_Word, letters_guessed):
#     '''
#     secretWord: string, the random word the user is trying to guess. This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: String, of letters and underscores. For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position. For letters
#     in the word that the user has not yet guessed, show an _ (underscore) instead.
#     '''
#
#     scrambledWord = "_" * len(load_word())
#
#     if


    # FILL IN YOUR CODE HERE...

def spaceman(secret_word):
    '''
    secretWord: String, the secret word to guess.

    Starts up a game of Spaceman in the command line.

    * At the start of the game, let the user know how many letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the partially guessed word so far, as well as the letters that the user has not yet guessed.
    '''

    # FILL IN YOUR CODE HERE...


secret_word = load_word()
spaceman(load_word())




secretWord = load_word()


from turtle import *


secretWord = "please"

def secretWordHidden():
    hiddenWord = list()
    hiddenWord.append(len(secretWord) * "_")
    return hiddenWord()

color('red', 'yellow')
write("please god", font=("Arial", 16, "normal"))
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
