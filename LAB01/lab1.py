
# --- 1 - rock paper scissors function --- #
def wins_rock_scissors_paper(s1, s2): 
    p1 = s1.upper()
    p2 = s2.upper()
    winning_hand = {
        'ROCK': 'SCISSORS',
        'PAPER': 'ROCK',
        'SCISSORS': 'PAPER'
    }
    if p1 == p2: 
        return False
    elif p1 in winning_hand and winning_hand[p1] == p2:
        return True
    else:
        return False

# making the string arguments uppercase to avoid casing issues, 
#then using a dictionary, store the winning hands. If p1 is any
#playable hand, check p2 in the same line to see if its win (return True)



# --- 2 - factorial function --- #
def factorial(n):
    result = 1
    if n == 0:
        return 1
    else:
        for x in range(1, n+1):
            result *= x 
        return result 

# range() creates a sequence of numbers, the brackets hold (start, stop)
#where the numbers begin at 'start' and up to (but excluding) 'stop'



# --- 3 - Fibonacci --- #
def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        for x in range(2, n+1):
            next = a + b
            a = b
            b = next
        return b    



# --- 4 - sum_to_goal --- #
def sum_to_goal(list, goal):
    for x in list:
        a = x
        y = x+1
        for y in list:
            b = y
            sum = a + b
            if(sum == goal):
                return a*b
    return 0



# --- 5 - UpCounter --- #
class UpCounter:

    def __init__(self, stepSize=1, counter=0):
        self.stepSize = stepSize
        self.counter = counter


    def count(self):
        return self.counter
    
    def update(self):
        self.counter += self.stepSize

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.stepSize







# --- --- REFLECTION --- ---
#While python functions in a similar way to C++, it is a higher level language and
#as a result makes the code much more readable and smaller in comparison to C++. For
#example, declaring variables in C++ requires you to specify the type of the variable. In
#python I dont have to do that. The for loop is another example of a tool that is much more
#simple in python in comparison to C++. 

#The entire structure and flow of python behaves differently from what I expected, for example 
#there are no semi-colons at all which was very off putting at first, each line is its own 
#statement automatically. Furthermore not having brackets when declaring an if-statement or 
#for-loop was very strange at first. These read more like a sentence then code now, if that
#makes sense.