#Bubble sort in python 

def bubSort(arr, size):
    swap = False
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            return


size = int(input("Enter the size of integer array : "))
arr = []
for i in range(size):
    n = int(input(f"arr[{i}] = "))
    arr.append(n)

print("Your unsorted array is : ", arr)
bubSort(arr, size)
print("Your sorted array is : ", arr)
