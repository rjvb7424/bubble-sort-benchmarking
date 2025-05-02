import matplotlib.pyplot as plt
import sort as python_sort

LIST_SIZE = 400
NUM_TRIALS = 5

python_results = []

for i in range(LIST_SIZE):
    result = python_sort.run(i, NUM_TRIALS)
    python_results.append(result)

x = list(range(LIST_SIZE))
y = python_results

plt.scatter(x, y)
plt.xlabel("Size of list")
plt.ylabel("Time to sort list (in seconds)")
plt.title("Bubble Sort Performance in Python")
plt.show()
