# Anyi Guo 03/10/2015 http://yanniey.github.io
# Mini Project #2 for “Guess the number” game
# An Introduction to Interactive Programming in Python (Part 1)

import random
import simplegui
import math

secret_number = 0
guess = 0
remaining_guess = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,remaining_guess
    input_guess()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number,remaining_guess
    secret_number= random.randrange(0,100)
    remaining_guess = 7
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number,remaining_guess
    secret_number = random.randrange(0,1000)
    remaining_guess = 10
    new_game()

# def counting_down():
#     global remaining_guess
#     remaining_guess -=1
#     print "Number of guesses remaining: %s" % remaining_guess
#     print ""
    
def input_guess():
    # main game logic goes here 
    global guess,remaining_guess
    guess = input("Please enter your guess:")

    # if user input "end" then end the guess
    if guess == "end":
        print "You end the game"
        return

    # test to make sure that input is a valid number
    try:
        guess = int(guess)
        print "Your guess was %s " % guess
    except ValueError:
        print "'%s' -  Please enter a valid number\n" %guess

    # compare the two numbers
        
    if remaining_guess > 0 or remaining_guess == 0 :
        if guess == secret_number:
            print "Your guess was correct"
            print ""
        else: 
            if guess > secret_number:
                print "Guess Lower"
                remaining_guess -=1
                print "Number of guesses remaining: %s" % remaining_guess
                print ""
                input_guess()
            else:
                print "Guess Higher"
                remaining_guess -=1
                print "Number of guesses remaining: %s" % remaining_guess
                print ""
                input_guess()
    else:
        print "You've run out of guesses. The secret number was %s" %secret_number
    
    
    
# create frame
frame = simplegui.create_frame("new frame",100,200)
frame.add_button("Range 100",range100)
frame.add_button("Range 1000",range1000)
frame.add_input("my input",input_guess,50)

# register event handlers for control elements and start frame


# call new_game 
frame.start()

# always remember to check your completed program against the grading rubric
