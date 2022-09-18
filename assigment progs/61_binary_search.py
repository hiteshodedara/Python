#Binary search in python...


def binarySearch(list, low, high, n):
    while low <= high:
        mid = (high + low) // 2

        if list[mid] > n:
            high = mid - 1
        elif list[mid] < n:
            low = mid + 1
        else:
            return mid
    else:
        return -1




list = [14, 17, 23, 32, 41, 43, 57, 59, 65, 68, 71, 72, 73, 75, 82, 86, 91, 95]
print("Here is a sorted list : ", list)
n = int(input("What do you want to search : "))

index = binarySearch(list, 0, len(list)-1, n)
if index != -1:
    print(n, " is on index ", index)
else:
    print("Can not find ", n)
