import matplotlib.pyplot as plt
import pandas as pd
import sort as python_sort
from time import perf_counter

LIST_SIZE = 500
NUM_TRIALS = 5

# Run Python benchmark
python_results = []
for i in range(LIST_SIZE):
    result = python_sort.run(i, NUM_TRIALS)
    python_results.append(result)

# Run python benchmark with built-in sort
python_results_builtin = []
for i in range(LIST_SIZE):
    data = python_sort.generate_random_numbers(i)
    start = perf_counter()
    sorted_data = sorted(data)
    total_time = perf_counter() - start
    python_results_builtin.append(total_time)

# Read C benchmark results
df_c = pd.read_csv("c_bubble_results.csv")

# X and Y for Python
x_python = list(range(LIST_SIZE))
y_python = python_results

# X and Y for Python with built-in sort
x_python_builtin = list(range(LIST_SIZE))
y_python_builtin = python_results_builtin

# X and Y for C (ensure sizes match)
x_c = df_c["ListSize"]
y_c = df_c["AverageTime"]

# Plot both
plt.figure(figsize=(10, 6))
plt.scatter(x_python, y_python, color="blue", label="Python Bubble Sort", s=10)
plt.scatter(x_c, y_c, color="purple", label="C Bubble Sort", s=10)
plt.scatter(x_python_builtin, y_python_builtin, color="yellow", label="Python Built-In Sort", s=10)

plt.xlabel("Size of list")
plt.ylabel("Time to sort list (in seconds)")
plt.title("Bubble Sort Performance: Python vs C")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
