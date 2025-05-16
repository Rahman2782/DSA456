
# rock paper scissors function
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



# factorial function
def factorial(i):
    result = 1
    if i == 0:
        return 1
    else:
        for x in range(1, i+1):
            result *= x 
        return result 

# range() creates a sequence of numbers, the brackets hold (start, stop)
#where the numbers begin at 'start' and up to (but excluding) 'stop'