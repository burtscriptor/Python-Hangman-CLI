import random
import words

# global variables
remaining_tries = 11
secret_word = None
clone = None
secret_word_len = None
guess = None
attempts = []
prog_string = None
num_occ = None
guess_loc = []
random_number = None

# functions
def init():
    print('Welcome to hangman, you all know the rules!')
    word_generator()
    print(secret_word)
    
    while True:
        if remaining_tries > 0:
            user_guess()
            check_guess()
            string_builder()
            win()
        else:
            print('Had by the hangman!')
            break
           
    
    
  
    
# ------------------
def word_generator():
    global random_number, secret_word, secret_word_len, clone, prog_string
    random_number = random.randrange(0, len(words.words))
    clone = secret_word = words.words[random_number]
    secret_word_len = len(secret_word)
    if prog_string is None:
        prog_string = ""
    i = 0    
    while i < secret_word_len:
        prog_string += "_"
        i += 1
    return

def user_guess():
    global guess, attempts
    guess = input('Enter a single character guess ')
    attempts.append(guess)
    return

def check_guess():
    global num_occ, guess_loc, remaining_tries
    if guess_loc is None:
        guess_loc = []
    num_occ = secret_word.count(guess) 
    if num_occ <= 0:
         remaining_tries -= 1
         print(f'{guess} did not appear in the secret word, you have {remaining_tries} tries remaining')
         print(f'You have tried {attempts} characters')
         return
    else:
         print('Good Guess!')
    i = 0
    while i < secret_word_len:
        if secret_word[i] == guess:
            guess_loc.append(i)
        i += 1       
    # print(f'this is {guess_loc}')
    return


def string_builder():
    global num_occ, guess_loc, guess, secret_word_len, prog_string
    # print(f'this clone {clone}')
   
    prog_string = list(prog_string) 
    i = 0
    while i < secret_word_len:
                if i in guess_loc:
                    prog_string[i] = guess
                i += 1     
    prog_string = ''.join(prog_string)
    guess_loc = None
    print(prog_string)
    
def win():
     if secret_word == prog_string:
          print('you have won')
     else:
          return True
          
# call functions
init()

