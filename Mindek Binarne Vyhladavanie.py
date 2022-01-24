import random
lol = 30
pole = []

for i in range(lol):
    if random.randint(0, 1):
        pole.append(i)


print(pole)

v = int(input("Zadaj cislo : "))

def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1
result = binary_search(pole, 0, len(pole) - 1, v)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



