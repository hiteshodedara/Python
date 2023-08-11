#Shell sort in python 

def shellSort(arr, size):
    gap = size//2
    
    while gap > 0:
        for i in range(gap,size):
            temp = arr[i]
            j = i

            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            arr[j] = temp
        gap //= 2
    return arr


size = int(input("Enter the size of integer array : "))
arr = []
for i in range(size):
    n = int(input(f"arr[{i}] = "))
    arr.append(n)

print("Your unsorted array is : ", arr)
print("Your sorted array is : ", shellSort(arr, size))
