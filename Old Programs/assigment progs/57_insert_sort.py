#Insertion sort in python 


def insertSort(arr, size):
    for i in range(1, size):
        k = arr[i]
        j = i-1

        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
        print(arr)
        input()
    return arr


size = int(input("Enter the size of integer array : "))
arr = []
for i in range(size):
    n = int(input(f"arr[{i}] = "))
    arr.append(n)

print("Your unsorted array is : ", arr)
print("Your sorted array is : ", insertSort(arr, size))
