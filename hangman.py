import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the words
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #USER GUESSES
    
    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join['a','b','c'] ---> 'a b c'
        print("you have ",lives," lives left you have used these letters",' '.join(used_letters))

        #we must now print thw word leaving the unguessed words
        word_list = [letter if letter in used_letters else '- ' for letter in word]
        print("the current word is ",' '.join(word_list))


        user_letter = input("guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 
                print("LEtter not in the word")


        elif user_letter in used_letters:
            print("You have already guessed it ")

        else:
            print("invalid character")
        
    #grts here when len(word_letters) == 0 OR  wwhen lives ==0
    if lives==0:
        print("you died , sorry the word was ",word)
    else:
        print("you guessed the right word,",word)


hangman()
