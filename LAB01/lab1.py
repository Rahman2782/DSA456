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

# loop begins at 2 because 0 and 1 are ruled out already, 'next' is the sum
# of the 2 most recent numbers in the sequence. b is then set to the next value
# in the sequence, and a is set to b's previous value.


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

# lists are essentially simplified arrays


# --- 5 - UpCounter --- #
class UpCounter:
    #attributes
    def __init__(self, stepSize=1, counter=0):
        self.stepSize = stepSize
        self.counter = counter
    #functions
    def count(self):
        return self.counter
    
    def update(self):
        self.counter += self.stepSize

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.stepSize

# def __init__ is used to decalre and define the member attributes
# of python classes, the keyword 'self' can be changed and member
# attributes are called within the class using this keyword 