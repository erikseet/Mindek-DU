import random
from timeit import default_timer as timer
arr = []
cas = timer()

for i in range(0,5000):
    if random.randint(0,1):
        arr.append(i)
        random.shuffle(arr)

def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print("Array ktory chceme zoradit: ", arr)
insertionSort(arr)
end = timer()
print("Zoradenie pomocou InsertionSortu trvalo: ", end - cas, "sekúnd.")
print("Zoradeny array InsertionSortu je: ",arr)