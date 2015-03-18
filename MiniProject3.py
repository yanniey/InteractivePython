# template for "Stopwatch: The Game"

# define global variables
import simplegui
counter= 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"

    
def start():
    tick()
    timer.start()

def stop():
    timer.stop()
 
def reset():
    global counter
    counter = 0
    tick()


# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    print counter
    counter += 1

# define draw handler
def draw(canvas):

    
# create frame
frame = simplegui.create_frame("Stopwatch",200,200)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
timer = simplegui.create_timer(100, tick)
# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
