import random
listSize = 50
rand_list = [random.randint(0,101) for val in range(listSize)]
rand_list.sort(reverse=True)
print("steps needed for sorting: {}".format(bubble_sort(rand_list)))

def bubble_sort(my_list):
  steps = 0
  for i in range(0, len(my_list) - 1):
    for j in range(0, len(my_list) - 1 - i):
      if my_list[j] > my_list[j + 1]:
        steps += 4 # 4 operations, 3 for the swap and one for the comparison
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
  return steps

def selection_sort(my_list):


def insertion_sort(my_list):


def quick_sort(mylist):


def insertion_sort(mylist, left, right):



def main:
