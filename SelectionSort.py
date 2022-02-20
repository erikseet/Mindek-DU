import sys
import random
from timeit import default_timer as timer
arr = []
cas = timer()

for i in range(0,5000):
    if random.randint(0,1):
        arr.append(i)
        random.shuffle(arr)

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

end = timer()
print("Array ktory chceme zoradit: ", arr)
print("Zoradenie pomocou SelectionSorteru trvalo: ", end - cas, "sekúnd.")
print("Zoradeny array Selectionsorterom je: ",arr)
