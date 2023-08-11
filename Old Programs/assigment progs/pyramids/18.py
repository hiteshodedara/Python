n = int(input("Enter the number of lines : "))


#for loop..
print("\nFor Loop...")
space = n
for i in range(1, n*4, 4):
    print(" "*space + "*"*i)
    space -= 1


#While loop..
print("\nWhile Loop...")
space = n
i = 1
while(i<n*4):
    print(" "*space + "*"*i)
    space -= 1
    i += 4
