n = int(input("Enter the number of lines : "))

space = n


#for loop..
print("\nFor loop...")
for i in range(int(1),n+1):
    print("*"*i+" "*space+"*"*i)
    space -= 1

#while loop...
print("\nWhile loop...")
i = int(1)
space = n
while(i<=n):
    print("*"*i+" "*space+"*"*i)
    space -= 1
    i += 1
