n = int(input("Enter the number of lines : "))


#for loop..
print("\nFor loop...")
i = 3*n+1
for space in range(n):
    print(" "*space + "*"*i)
    i -= 4


#while loop..
print("\nWhile loop...")
i = 3*n+1
space = int(0)
while (space < n):
    print(" "*space + "*"*i)
    i -= 4
    space += 1
