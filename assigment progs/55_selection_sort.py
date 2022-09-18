from platform import java_ver


def selSort(arr, size):
    for index in range(size):
        minimum = index
    
        for i in range(index + 1, size):
            if arr[i] < arr[minimum]:
                minimum = i
        (arr[index], arr[minimum]) = (arr[minimum],arr[index])
    return arr


size = int(input("Enter the size of integer array : "))
arr = []
for i in range(size):
    n = int(input(f"arr[{i}] = "))
    arr.append(n)

print("Your unsorted array is : ", arr)
print("Your sorted array is : ", selSort(arr, size))
