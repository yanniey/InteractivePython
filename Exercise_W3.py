# Timers (Week 3b) Exercise 2

# Given the solution from the following problem, we again want a counter printed to the console. Add three buttons that start, stop and reset the counter, respectively.


# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    
def start():
    tick()
    timer.start()

def stop():
    timer.stop()
 
def reset():
    global counter
    counter = 0
    tick()
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start",start, 100)
frame.add_button("Stop",stop, 100)
frame.add_button("Reset",reset,100)
timer = simplegui.create_timer(1000, tick)

# Start timer
frame.start()

# Timers (Week 3b) Exercise 3

# Use a timer to toggle the canvas background back and forth between red and blue every 3 seconds. Use the CodeSkulptor Docs to locate the appropriate call to change the background color of the canvas.
# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = "Red"

 
# Timer handler
def tick():
    global color 
    if color == "Red":
        color = "Blue"
    elif color == "Blue":
        color = "Red"
    frame.set_canvas_background(color)
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_canvas_background(color)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()



# Timers (Week 3b) Exercise 4

# Create a circle in the center of the canvas. Use a timer to increase its radius one pixel every tenth of a second.

# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def timer():
    global radius
    radius += 1
    
# Draw handler
def draw(canvas):
    global radius
    canvas.draw_circle((100, 100), radius, 12, 'Green','Green')
    
        
# Create frame and timer
frame = simplegui.create_frame("Frame",WIDTH,HEIGHT)
timer = simplegui.create_timer(100,timer)
frame.set_draw_handler(draw)
# Start timer
frame.start()
timer.start()
