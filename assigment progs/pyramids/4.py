n = int(input("Enter the number of lines : "))


#for loop
print("\nfor loop..")
i = n
for space in range(n):
    print(" "*space,"*"*i)
    i-=1


#while loop..
print("\nWhile loop...")
i = n
space = int(0)

while(space < n):
    print(" "*space,"*"*i)
    i-=1
    space += 1
