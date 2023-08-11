n = int(input("Enter the number of lines : "))


#for loop..
print("\nFor loop..")
space = 0

for i in range (n, 0, -1):
    print("*"*i + " "*space + "*"*i + " "*space + "*"*i + " "*space + "*"*i)
    space += 1

#while loop..
print("\nWhile loop...")
space = 0
i = n
while(i>=0):
    print("*"*i + " "*space + "*"*i + " "*space + "*"*i + " "*space + "*"*i)
    space += 1
    i -= 1
