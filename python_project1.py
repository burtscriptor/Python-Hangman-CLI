import random 


#  lets write a number guessing game
#  ask the user to guess a number between 1- 20
#  need to randomise a number first and store it in a variable
#  then use a loop to check in the user guess = the number
#  if it dose not then ask again for another number
#  maybe give hints
#  else print a msg to say they guess the number and would they like to play again

def number_guessing_game():

    guessed = []

    random_number = random.randrange(1,20)
    print(random_number)
    guess = input('Enter a guess between 1- 20 ')
    guess = int(guess)
    guessed.append(guess)

    while guess != random_number:
        print(f'Guess again, these are the numbers you have tried {guessed}')
        guess = input()
        guess = int(guess)
        guessed.append(guess)
    if guess == random_number:
        print(f'Congratulations you guessed correctly! You took {len(guessed)} but got there!')
    

   


number_guessing_game()