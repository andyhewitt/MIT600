# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!


    
import string

def insert_blank(word):
    l = []
    for i in range(len(word)):
        l.append('-')
    return l

#check if the input is correct，return true if correct.
def is_correct(guess, word, wor_compare):

    n = len(word)
    for i in range(n):
        if guess == wor_compare[i]:
            return True
    return False

#return an index of the input.
def return_index(guess, word, wor_compare):
    n = len(word)
    for i in range(n):
        if guess == wor_compare[i]:
            return i


def insert_letter(l, word, guess):
    result = ''
    for letter in l:
        if letter in guess:
            result = result + letter
        else:
            result = result + '_'
        

##
##def insert_letter(l, guess, word):
##    
##    i = return_index(guess, word, wor_compare)
##    l[i] = word[i]
##    for i in l:
##        print(i,end = '')

def insert_blank_to_word(wor_compare):
    i = return_index(guess, word, wor_compare)
    wor_compare[i] = '-'
    return 
        
def current_letter(l):
    for i in l:
        print(i,end = '')

def avaliable(l, s, wor_compare):

    for i in l:
        if i in s and i not in wor_compare:
            s.remove(i)
    for i in s:
        print(i, end = '')

def word_compare_str(word):
    wor_compare = []
    for i in range(len(word)):
        wor_compare.append(word[i])
    return wor_compare

       
#program start##
word = choose_word(wordlist)

#avaliable string create
s = []
s = list(string.ascii_lowercase)
l = insert_blank(word)
wor_compare = word_compare_str(word)


print('Welcome to the game, Hangman!' +\
        'I am thinking of a word that is ' +\
         str(len(word)) + ' letters long.')

origin = word_compare_str(word)
times = 10
word_enter = []
#check if the guess is correct
while times > 0:
    if l != origin:
        print('You have ' + str(times) + ' guesses left!')
        print('Avaliable letters: ', end = '')
        avaliable(l, s, wor_compare)
        print('')
        guess = str(input('Please guess a letter: '))
        word_enter.append(guess)
        if is_correct(guess, word, wor_compare):
            print('Good guess:', end = '')
            insert_letter(l, guess, word)
            insert_blank_to_word(wor_compare)
            print('')
            print('word you have entered:', word_enter)
        else:
            print('Oops! That letter is not in my word:', end = '')
            current_letter(l)
            print('')
            print('word you have entered:', word_enter)
            times -= 1
    else:
        print('Congratulations, you won!!')
    
print('You lose, the word is: ', end = '')
print(word)
