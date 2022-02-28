import random
from timeit import default_timer as timer
import copy

arr = random.sample(range(50001), 50001)

print("Array ktory chceme zoradit: ",arr)

arr0 = copy.deepcopy(arr)
arr1 = copy.deepcopy(arr)
arr2 = copy.deepcopy(arr)
arr3 = copy.deepcopy(arr)
arr4 = copy.deepcopy(arr)


start_quicksort = timer()
def partition(arr0, low, high):
    i = (low - 1)
    pivot = arr0[high]

    for j in range(low, high):
        if arr0[j] <= pivot:
            i = i + 1
            arr0[i], arr0[j] = arr0[j], arr0[i]

    arr0[i + 1], arr0[high] = arr0[high], arr0[i + 1]
    return (i + 1)

def quickSort(arr0, low, high):
    if len(arr0) == 1:
        return arr0
    if low < high:
        pi = partition(arr0, low, high)
        quickSort(arr0, low, pi - 1)
        quickSort(arr0, pi + 1, high)
n = len(arr0)
quickSort(arr0, 0, n - 1)
end = timer()
cas_quicksorter = end - start_quicksort
print("Zoradený array je: ", arr,)
print("Rýchlosť quick sorteru je: ",cas_quicksorter, "sekund.")

arr_bubble = arr1
start_bubblesorter = timer()
def bubbleSort(arr1):
    n = len(arr1)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

bubbleSort(arr1)
end_bubblesorter = timer()
cas_bubblesorter = end_bubblesorter - start_bubblesorter
print("Rýchlosť bubble sorteru je: ",cas_bubblesorter, "sekund.")

arr_insertion = arr2
start_insertionsorter = timer()
def insertionSort(arr2):
    for i in range(1, len(arr2)):

        key = arr2[i]
        j = i - 1
        while j >= 0 and key < arr2[j]:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
insertionSort(arr2)
end3 = timer()
cas_insertionsort = end3 - start_insertionsorter
print("Rýchlosť insertion sorteru je: ",cas_insertionsort, "sekund.")


arr_merge = arr3
start_mergesorter = timer()
def mergeSort(arr3):
    if len(arr3) > 1:
        mid = len(arr3) // 2
        L = arr3[:mid]
        R = arr3[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr3[k] = L[i]
                i += 1
            else:
                arr3[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr3[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    mergeSort(arr3)
    end4 = timer()
    cas_mergesorter = end4 - start_mergesorter
    print("Rýchlosť merge sorteru je: ",cas_mergesorter, "sekund.")


arr_selection = arr4
start_selectionsort = timer()
for i in range(len(arr4)):
    min_idx = i
    for j in range(i + 1, len(arr4)):
        if arr4[min_idx] > arr4[j]:
            min_idx = j
    arr4[i], arr4[min_idx] = arr4[min_idx], arr4[i]

end5 = timer()
cas_selectionsorter = end5 - start_selectionsort
print("Rýchlosť selection sorteru je: ",cas_selectionsorter, "sekund.")

