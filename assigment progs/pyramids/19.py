n = int(input("Enter the number of lines : "))

#for loop...
print("\nFor loop...")
i = 1
for space in range(n*3+1, 1, -3):
    print(" "*space + "*"*i)
    i += 4


#while loop..
print("\nWhile loop...")
i = 1
space = n*3+1
while(space > 1):
    print(" "*space + "*"*i)
    i += 4
    space -= 3
