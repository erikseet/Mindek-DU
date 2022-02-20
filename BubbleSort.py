import random
from timeit import default_timer as timer

cas = timer()

arr = []
for i in range(0,5000):
    if random.randint(0,1):
        arr.append(i)
        random.shuffle(arr)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(arr)
end = timer()
print("Zoradenie pomocou BubbleSortu trvalo: ", end - cas, "sekúnd.")
print("Zoradeny array BubbleSortu je: ",arr)