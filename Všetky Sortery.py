import random
from timeit import default_timer as timer

arr = random.sample(range(5000), 5000)

print("Array ktory chceme zoradit: ",arr)

arr_bubble = arr
arr_quicksort = arr
arr_merge = arr
arr_selection = arr
arr_insertion = arr



start_quicksort = timer()
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
n = len(arr)
quickSort(arr, 0, n - 1)
end = timer()
cas_quicksorter = end - start_quicksort




start_bubblesorter = timer()
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(arr)
end_bubblesorter = timer()
cas_bubblesorter = end_bubblesorter - start_bubblesorter



start_insertionsorter = timer()
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
cas_insertionsort = end3 - start_insertionsorter


start_mergesorter = timer()
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
    cas_mergesorter = end4 - start_mergesorter

start_selectionsort = timer()
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

end5 = timer()
cas_selectionsorter = end5 - start_selectionsort



print("Zoradené pole je: ", arr_bubble, "sek.")
print("Rýchlosť quick sorteru je: ",cas_quicksorter, "sekund.")
print("Rýchlosť insertion sorteru je: ",cas_insertionsort, "sekund.")
print("Rýchlosť merge sorteru je: ",cas_mergesorter, "sekund.")
print("Rýchlosť selection sorteru je: ",cas_selectionsorter, "sekund.")
print("Rýchlosť bubble sorteru je: ",cas_bubblesorter, "sekund.")
