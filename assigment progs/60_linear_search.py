#Linear search in python 

def linearSearch(list, n):
    find = False
    for i in range(len(list)):
        if n == list[i]:
            print(n, " is on the index ", i)
            find = True
    if not find:
        print("Can't find ", n)
        




list = [55,81,24,9,36,75,85,74,13]

print("Here is the list : ", list)
n = int(input("Which element do you want to search : "))

linearSearch(list, n)
