n = int(input("Enter the number of lines : "))


#for loop..
print("\nFor loop...")
i = 2*n+3
space = 0
for a in range(n):
    print(" "*space + "*"*i)
    i -= 3
    space += 2


#while loop..
print("\nWhile loop...")
i = 2*n+3
space = int(0)
a = 0
while (a < n):
    print(" "*space + "*"*i)
    i -= 4
    space += 3
    a += 1
