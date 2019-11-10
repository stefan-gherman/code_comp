#A program that prompts the user to guess the number that the computer chose.

import random  #Module import

guesses_taken = 0 #Variable initialization

print('Hello! What is your name?')
myName = input() #myName is assigned to the return statement of the input() function

number = random.randint(1, 20) #a random number between 1, 20 is generated
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6: #A loop that goes until the number of guesses has reached 6.
    print('Take a guess.')
    guess = input()  
    guess = int(guess) #The guess is transformed from string, the output on input() into an int 

    guesses_taken += 1 #guess_taken is incremented

    if guess < number: #If statement checking the user guess against the computer choice
        print('Your guess is too low.') 

    if guess > number:
        print('Your guess is too high.')

    if guess == number: #If the user has guessed correctly the number the loop will be stopped via the break statement
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') 
    '''
    Based on what value the guess(equal or not equal to computer choice) variable will have a message will be printed. 
    '''

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
