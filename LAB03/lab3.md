# PART B: ANALYSIS
## Function 1
    def function1(value, number):
        if (number == 0):
            return 1
        elif (number == 1):
            return value
        else:
            return value * function1(value, number-1)
- **Time Complexity: O(n)** - a linear number of recursive calls are made relative to 'number'. There is a constant amount of work being performed at each call of the function.
- **Space Complexity: O(n)** - each time 'function1' is called a new stack frame is pushed onto the stack, each stack stores value and number which are constants (k) -> n*k results in O(n) space because of the depth of recursion.

## Function 2
    def recursive_function2(mystring,a, b):
        if(a >= b ):
            return True
        else:
            if(mystring[a] != mystring[b]):
                return False
            else:
                return recursive_function2(mystring,a+1,b-1)
    
    def function2(mystring):
        return recursive_function2(mystring, 0,len(mystring)-1)
- **Time Complexity: O(n)** - 'n' is the length of 'mystring' and performs a constant amount of work at each recursion. As 'n' gets bigger, so does the number of steps, there is a direct correlation here. 
- **Space Complexity: O(n)** - the total memory on the stack grows with directly with 'n'. 

## Function 3
    def function3(value, number):
        if (number == 0):
            return 1
        elif (number == 1):
            return value
        else:
            half = number // 2
            result = function3(value, half)
            if (number % 2 == 0):
                return result * result
            else:
                return value * result * result
- **Time Complexity: O(log n)** - The size of the problem is cut in half on each recursion making this function very efficient 
- **Space Complexity: O(log n)** - the space grows logarithmically with its input and stores constant memory for its local variables.
- Lets say 'n' (number) was equal to 16, if the base cases are not met then half = 16 // 2 (8). This would continue to 4, 2, 1. The value of log8 is 3 which is how many calls deep we are in recursion. 

# PART C: REFLECTION
### 1. Describe how to approach writing recursive functions; what steps do you take?
- When working with recursive functions, the goal is to solve a problem by breaking it down into smaller versions of itself. Each recursive function has a base case, the goal is to make each function call move closer to meeting the condition of the base case. 
### 2. Describe the process of analyzing recursive functions. How does it differ from analyzing non-recursive functions? How is it the same?
- When analayzing space complexity for a recursive function, the call stack has to be considered since at every recursive call a new frame is added to the stack. We want to find how many calls there are on the stack at its deepest point. When compared with non-recurisve functions, you count operations directly by looking at loop iterations. 
- For time complexity, you want to focus on looking at smaller recursive calls and whats done at each level of recursion. The main distinction is in how the steps are counted for the 2 types of functions. Non-recursive functions focus heavily on loops (nested loops are generally N^2 while one loop is just N). We look at how many times a code block executes. For recursion this doesnt work because the function is calling itself.