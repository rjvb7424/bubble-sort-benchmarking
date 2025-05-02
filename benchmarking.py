import matplotlib.pyplot as plt
import pandas as pd
import sort as python_sort

LIST_SIZE = 400
NUM_TRIALS = 5

# Run Python benchmark
python_results = []
for i in range(LIST_SIZE):
    result = python_sort.run(i, NUM_TRIALS)
    python_results.append(result)

# Read C benchmark results
df_c = pd.read_csv("c_bubble_results.csv")

# X and Y for Python
x_python = list(range(LIST_SIZE))
y_python = python_results

# X and Y for C (ensure sizes match)
x_c = df_c["ListSize"]
y_c = df_c["AverageTime"]

# Plot both
plt.figure(figsize=(10, 6))
plt.scatter(x_python, y_python, color="blue", label="Python Bubble Sort", s=10)
plt.scatter(x_c, y_c, color="purple", label="C Bubble Sort", s=10)

plt.xlabel("Size of list")
plt.ylabel("Time to sort list (in seconds)")
plt.title("Bubble Sort Performance: Python vs C")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
