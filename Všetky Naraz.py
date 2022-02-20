import random
from timeit import default_timer as timer

cas = timer()
arr = []
for i in range(0,5000):
    if random.randint(0,1):
        arr.append(i)
        random.shuffle(arr)

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
end = timer()

print("Array ktory chceme zoradit: ",arr)
n = len(arr)
quickSort(arr, 0, n - 1)
print("Zoradeny array QuickSortu: ",arr)
print("Zoradenie pomocou QuickSortu trvalo: ", end - cas, "sekúnd.")



def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(arr)
end1 = timer()
print("Zoradeny array BubbleSortu je: ",arr)
print("Zoradenie pomocou BubbleSortu trvalo: ", end1 - cas, "sekúnd.")



for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

end2 = timer()
print("Zoradeny array BubbleSortu je: ",arr)
print("Zoradenie pomocou BubbleSortu trvalo: ", end2 - cas, "sekúnd.")


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertionSort(arr)
end3 = timer()
print("Zoradeny array InsertionSortu je: ",arr)
print("Zoradenie pomocou InsertionSortu trvalo: ", end3 - cas, "sekúnd.")


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    mergeSort(arr)
    end4 = timer()
    print("Zoradeny array MergeSortu je: ",arr)
    print("Zoradenie pomocou MergeSortu trvalo: ", end4 - cas, "sekúnd.")

lol = [end - cas,end1 - cas,end2 - cas,end3 - cas,end4 - cas]
lol.sort(reverse=True)
print("Zoradene od najvačšieho:", lol)