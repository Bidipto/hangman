
from string import ascii_lowercase
from words import get_random_word
 
 
def get_num_attempts():
    while True:
        num_attempts = int(input('How many incorrect attempts do you want? [1-25] '))
        if 1 <= num_attempts <= 25:
            return num_attempts
        else:
            print('{0} is not between 1 and 25'.format(num_attempts))

 
def get_min_word_length():
    while True:
        min_word_length = input('What minimum word length do you want? [4-16] ')
        try:
            min_word_length = int(min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print('{0} is not between 4 and 16'.format(min_word_length))
        except ValueError:
                print('{0} is not an integer between 4 and 16'.format(min_word_length))

def get_display_word(word, idxs):
    for i in range(len(word)):
        if idxs[i]==True:
            print(word[i],end="")
        else:
            print("*",end="")

def get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
        return next_letter

def playhangman():
    print('Starting a game of Hangman...')
    attempts_remaining = get_num_attempts()
    min_word_length = get_min_word_length()
    print('Selecting a word...')
    word = get_random_word(min_word_length)
    print()
    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False
    # Main game loop
    while attempts_remaining > 0 and not word_solved:
        print('Word:',end="")
        get_display_word(word, idxs)
        print("\n")
        print('Attempts Remaining: {}'.format(attempts_remaining))
        print('Previous Guesses: {}'.format(' '.join(wrong_letters)))
 
 
        next_letter = get_next_letter(remaining_letters)
        if next_letter in word:
            print('{0} is in the word!'.format(next_letter))
 
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
        
            print('{0} is NOT in the word!'.format(next_letter))
 
            attempts_remaining -= 1
            wrong_letters.append(next_letter)
 
        
        if False not in idxs:
            word_solved = True
        print()
 
    
    print('The word is {0}'.format(word))
 
    if word_solved:
        print('Congratulations! You won!')
    else:
        print('Try again next time!')
 
    try_again = input('Would you like to try again? [y/Y] ')
    return try_again.lower() == 'y'
 
 
while playhangman():
    print()