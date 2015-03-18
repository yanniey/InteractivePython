# Question 6
#How many instances of the letter "l" are there in the following:

#1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1
#Although it might be hard to tell, that string contains ones (1) and lower-case L's (l). Create a small CodeSkulptor program, and use copy-and-paste to put this string in your code. Your program should only need one function or method call.

str = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"
count = 0
for n in str:
    global count
    if n == "l":
        count +=1
        
# Question 9

#Turn the following description into a CodeSkulptor program, and run it.

#Create a 300-by-300 canvas.
#Draw two circles with radius 20 and white lines of width 10. One is centered at (90,200) and one at (210,200).
#Draw a red line of width 40 from (50,180) to (250,180).
#Draw two red lines of width 5 from (55,170) to (90,120) and from (90,120) to (130,120).
#Draw a red line of width 140 from (180,108) to (180,160).

import simplegui

def draw_handler(canvas):
    canvas.draw_circle([90, 200], 20, 10, 'White')
    canvas.draw_circle([210, 200], 20, 10, 'White')
    canvas.draw_line([50,180], [250,180], 40, 'Red')
    canvas.draw_line([55,170],[90,120],5,'Red')
    canvas.draw_line([90,120],[130,120],5,'Red')
    canvas.draw_line([180,108],[180,160],140,'Red')

    
frame = simplegui.create_frame('new', 300, 300)
frame.set_draw_handler(draw_handler)
frame.start()

