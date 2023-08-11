#Quick sort in python

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)



size = int(input("Enter the size of integer array : "))
array = []
for i in range(size):
    n = int(input(f"arr[{i}] = "))
    array.append(n)

print("Your unsorted array is : ", array)
quickSort(array, 0, size-1)
print("Your sorted array is : ", array)
