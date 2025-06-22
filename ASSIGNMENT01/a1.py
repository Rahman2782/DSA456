import random
import time
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(10**6)  #this will increase the recursion limit and prevent an error

# CREATING THE FUNCTIONS
def create_list(size, scenario="random"):
    if scenario == "random":
        return [random.randint(0, 100) for _ in range(size)]
    elif scenario == "best":
        return list(range(size))
    elif scenario == "worst":
        return list(range(size - 1, -1, -1))

def is_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

def bubble_sort(l):
    steps = 0
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            steps += 1
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                steps += 3
    return steps

def selection_sort(l):
    steps = 0
    for i in range(len(l) - 1):
        min_idx = i
        steps += 1
        for j in range(i + 1, len(l)):
            steps += 1
            if l[j] < l[min_idx]:
                min_idx = j
                steps += 1
        if min_idx != i:
            l[i], l[min_idx] = l[min_idx], l[i]
            steps += 3
    return steps

def insertion_sort(l):
    steps = 0
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        steps += 2
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
            steps += 3
        l[j + 1] = key
        steps += 1
    return steps

def quick_sort(l):
    steps = [0]
    def quicksort_recursive(low, high):
        if low < high:
            pivot, s = partition(low, high)
            steps[0] += s
            quicksort_recursive(low, pivot - 1)
            quicksort_recursive(pivot + 1, high)
    def partition(low, high):
        pivot = l[high]
        i = low - 1
        s = 2
        for j in range(low, high):
            s += 1
            if l[j] <= pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
                s += 4
        l[i + 1], l[high] = l[high], l[i + 1]
        s += 3
        return i + 1, s
    quicksort_recursive(0, len(l) - 1)
    return steps[0]

def insertion_sort_subarray(l, left, right):
    steps = 0
    for i in range(left + 1, right + 1):
        key = l[i]
        j = i - 1
        steps += 2
        while j >= left and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
            steps += 3
        l[j + 1] = key
        steps += 1
    return steps

# STEP 1 : SORT LIST
#===================
def main_step_1():
    print("\nSTEP 1\n==========\n")
    lst = create_list(100, "random")
    for name, func in {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Insertion Sort (Subarray)": lambda l: insertion_sort_subarray(l, 0, len(l)-1)
    }.items():
        test_list = list(lst)
        steps = func(test_list)
        print(f"{name}: Sorted = {is_sorted(test_list)}, T(n) = {steps}")

# STEP 2 : BEST + WORST CASE
#===========================
def main_step_2():
    print("\nSTEP 2\n==========")
    cases = ["best", "random", "worst"]
    funcs = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Insertion Sort (Subarray)": lambda l: insertion_sort_subarray(l, 0, len(l)-1)
    }
    for name, func in funcs.items():
        print(f"\n{name}")
        for case in cases:
            lst = create_list(100, case)
            steps = func(list(lst))
            print(f"  {case.capitalize()} Case: T(n) = {steps}")

# STEPS 3 + 4 : PLOTTING 
#=======================
def main_step_3_and_4():
    sizes = [10, 50, 100, 500, 1000, 5000]
    funcs = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick": quick_sort,
        "Subarray": lambda l: insertion_sort_subarray(l, 0, len(l)-1)
    }
    tn = {k: [] for k in funcs}
    times = {k: [] for k in funcs}

    for size in sizes:
        print(f"\nSize = {size}")
        for name, func in funcs.items():
            lst = create_list(size, "worst")
            start = time.time()
            steps = func(list(lst))
            end = time.time()
            tn[name].append(steps)
            times[name].append(end - start)
            print(f"{name}: T(n) = {steps}, Time = {end - start:.4f}s")

    plt.figure()
    for name in funcs:
        plt.plot(sizes, tn[name], label=name)
    plt.title("T(n) vs N (Worst Case)")
    plt.xlabel("List Size (N)")
    plt.ylabel("Operations T(n)")
    plt.legend()
    plt.savefig("tn_vs_n.png")

    plt.figure()
    for name in funcs:
        plt.plot(sizes, times[name], label=name)
    plt.title("Time vs N (Worst Case)")
    plt.xlabel("List Size (N)")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.savefig("time_vs_n.png")

if __name__ == "__main__":
    main_step_1()
    main_step_2()
    main_step_3_and_4()
