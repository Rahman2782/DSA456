# PART A: RECURSIVE FUNCTIONS
#=========================================================
# FUNCTION 1
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)

# FUNCTION 2
def linear_search(list, key):
    return linear_search_2(list, 0, key)

def linear_search_2(list, index, key):
    if list == []:
        return -1
    if list[0] == key:
        return index
    return linear_search_2(list[1:], index+1, key) 

# FUNCTION 3
def binary_search(list, key):
    return binary_search_2(list, 0, len(list)-1, key)

def binary_search_2(list, l, r, key):
    if l > r:
        return -1
    m = (l+r) // 2
    if list[m] == key:
        return m
    elif list[m] > key:
        return binary_search_2(list, l, m-1, key)
    elif list[m] < key:
        return binary_search_2(list, m+1, r, key)



#Part B to be done in .md file