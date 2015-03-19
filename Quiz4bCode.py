# Q9 Write a Python program that initializes a global variable to 5. The keydown event handler updates this global variable by doubling it, while the keyup event handler updates it by decrementing it by 3.

# What is the value of the global variable after 12 separate key presses, i.e., pressing and releasing one key at a time, and repeating this 12 times in total?

# To test your code, the global variable's value should be 35 after 4 key presses.

import simplegui

count = 5

def keyup(key):
	global count
	count = 2 * count
	if key == simplegui.KEY_MAP["up"]:
		count -= 3
	print count 


def draw(canvas):
    canvas.draw_text(str(count),(20,20),12, "White")

frame = simplegui.create_frame("untitled", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyup)

# start frame
frame.start()



def keydown(key):
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc