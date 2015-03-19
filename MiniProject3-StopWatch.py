# template for "Stopwatch: The Game"

import simplegui

# define global variables
width = 300
height = 300
position = [100,100]
interval = 100
time = 0
start_timer = 0



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    A = time / 600
    B = time % 600 / 100
    C = time % 100 / 10 
    D = time % 10
    result = str(A) + ":" + str(B) + str(C) + "." + str(D) 
    return result
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global start_timer
    tick()
    timer.start()
    start_timer = 1

def Stop():
    global time, start_timer
    if start_timer == 1:
        timer.stop()
        start_timer = 0
    else:
        pass

def Reset():
    global time
    time = 0
    return

def Quit():
    frame.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time +=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position, 36, "Green")
    

    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.add_button("Quit",Quit, 100)

# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
