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


# Function 2
#-----------------------
def function2(number):
	return (number * (number + 1) * (2 * number + 1)) // 6
# Time Complexity = O(1) - constant growth
# Space Complexity = O(1) - constant 


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


# Function 4
#-----------------------
def function4(number):
	total = 1
	for i in range(1, number):
		total *= i + 1
	return total
# Time Complexity = O(n) - liner growth
# Space Complexity = O(1) - constant
