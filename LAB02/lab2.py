# Function 1
#-----------------------
def function1(number):
	total = 0
 
	for i in range(number):
		x = i + 1
		total += x * x
 
	return total
# Time Complexity = O(n) - linear growth
# Space Complexity = O(1) - constant 

# The loop runs 'number' amount of times and the operations within the loop are constant,
# the variables declared in the function are also constant.


# Function 2
#-----------------------
def function2(number):
	return (number * (number + 1) * (2 * number + 1)) // 6
# Time Complexity = O(1) - constant growth
# Space Complexity = O(1) - constant 

# There is a fixed number of operations to be performed in the function and the input
# (number) will not affect the time and space complexity as a result.


# Function 3
#-----------------------
def function3(list):
	n = len(list)
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if list[j] > list[j+1]:
				tmp = list[j]
				list[j] = list[j+1]
				list[j + 1] = tmp
# Time Complexity = O(n^2) - quadratic growth
# Space Complexity = O(1) - constant

# This function is a bubble sort, when there is a for loop nested in another for loop it 
# creates a grid of 'n'(length of 'list'), this results in quadratic growth or O(n^2) growth.
# 'n' is affected by 'list' while tmp is constant  in this function.

# Function 4
#-----------------------
def function4(number):
	total = 1
	for i in range(1, number):
		total *= i + 1
	return total
# Time Complexity = O(n) - liner growth
# Space Complexity = O(1) - constant
<<<<<<< HEAD

# The loop will iterate 'number' times and each iteration performs constant operations with the
# variables in the function all using a constant amount of space.
=======
>>>>>>> a0db49d3723c200b7d516f52a6067ca34efe1e8a
