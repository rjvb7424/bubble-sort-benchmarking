# Bubble sort benchmark

import random
from time import perf_counter

MAX_VALUE = 999999
SIZE = 5000
NUM_TRIALS = 5


def generate_random_numbers(size):
    return list(random.randint(1, MAX_VALUE) for i in range(size))


# implementation to be completed here
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


total_time = 0.0

for i in range(NUM_TRIALS):
    data = generate_random_numbers(SIZE)
    start = perf_counter()
    bubble_sort(data)
    total_time += perf_counter() - start

average_time = total_time / NUM_TRIALS
print(f"{SIZE} numbers sorted in {average_time:.3f} seconds")
