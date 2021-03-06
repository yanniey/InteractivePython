# Q6 Find epoch time
import time

time.gmtime(0)[0]

# Q8 Collatz conjecture

Given any initial natural number, consider the sequence of numbers generated by repeatedly following the rule:

divide by two if the number is even or
multiply by 3 and add 1 if the number is odd.
The Collatz conjecture states that this sequence always terminates at 1. For example, the sequence generated by 23 is:

23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

Write a Python program that takes a global variable n and uses a timer callback to repeatedly apply the rule above to n. Use the code from the previous question as a template. I suggest that your code prints out the sequence of numbers generated by this rule. Run this program for n = 217. What is the largest number in the sequence generated by this starting value?

To test your code, starting at n = 23 generates a sequence with a maximum value of 160.



import simplegui


result = 1
biggest = 0
iteration = 0
max_iterations = 10

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
	global n, biggest
	if n % 2 == 0:
		n = n/2
	else:
		n = n * 3 + 1

	if n > biggest:
		biggest = n

	# print n

# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration, result, biggest
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", biggest
    else:
        result = get_next(result)

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(217)
timer.start()


# the answer is 736
