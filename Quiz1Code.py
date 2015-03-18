# An Introduction to Interactive Programming in Python (Part 1) 
# Rice University
# Coursera 02/23/2015

# question 6
#Implement the mathematical function f(x) = -5 x5 + 69 x2 - 47 as a Python function. Then use Python to compute the function values f(0), f(1), f(2), and f(3). Enter the maximum of these four numbers.

def function(x):
  y= -5 *(x**5) + 69 *(x**2) - 47
  return y
   
print max(function(0),function(1),function(2),function(3))

print function(0)
print function(1)
print function(2)
print function(3)

# question 7
#When investing money, an important concept to know is compound interest. The equation FV = PV (1+rate)periods relates the following four quantities.

#The present value (PV) of your money is how much money you have now.
#The future value (FV) of your money is how much money you will have in the future.
# The nominal interest rate per period (rate) is how much interest you earn during a particular length of time, before accounting for compounding. This is typically expressed as a percentage.
# The number of periods (periods) is how many periods in the future this calculation is for.
# Finish the following code, run it, and submit the printed number. Provide at least four digits of precision after the decimal point.

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    fv = present_value*(1+rate_per_period)**periods
    return fv
    
    
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)


# question 8

def area(n,s):
    area = (0.25*n*(s**2) ) / math.tan(math.pi/n)
    return area
    
print area(7,3)


# question 10
# The following code has a number of syntactic errors in it. The intended math calculations are correct, so the only errors are syntactic. Fix the syntactic errors.

import math

def project_to_distance(point_x,point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale
    
print project_to_distance(2, 7, 4)