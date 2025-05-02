# External imports
import random
from time import perf_counter

# Constants
MAX_VALUE = 999999
NUM_TRIALS = 5

# Generate random numbers
def generate_random_numbers(size):
    return list(random.randint(1, MAX_VALUE) for i in range(size))

# Bubble Sort Implementation
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break 

# Function that will be called from the main program
def run(list_size, num_trials):
    bubble_sort_tests = []
    average_time = 0
    for i in range(num_trials):
        data = generate_random_numbers(list_size)
        start = perf_counter()
        bubble_sort(data)
        total_time = perf_counter() - start
        bubble_sort_tests.append(total_time)
        average_time = sum(bubble_sort_tests) / num_trials
    return average_time