
# rock paper scissors function
def wins_rock_scissors_paper(s1, s2):
    p1 = s1.upper()
    p2 = s2.upper()
    match p1:
        case 'ROCK':
            if p2 == 'SCISSORS':
                return 1 
            elif p2 == 'PAPER':
                return 0
            elif p2 == 'ROCK':
                return 0
        case 'PAPER':
            if p2 == 'SCISSORS':
                return 0 
            elif p2 == 'PAPER':
                return 0
            elif p2 == 'ROCK':
                return 1
        case 'SCISSORS':
            if p2 == 'SCISSORS':
                return 0 
            elif p2 == 'PAPER':
                return 1
            elif p2 == 'ROCK':
                return 0

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