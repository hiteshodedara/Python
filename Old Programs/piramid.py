n = int(input("Enter the number of lines : "))


#for loop..
print("\nFor loop..")
space = n+1

for i in range (0, n+1,1):
    print( "*"*i + " "*space + "*"*i + " "*space + "*"*i + " "*space + "*"*i)
    space -= 1

#while loop..
print("\nWhile loop...")
space = n
i = int(1)
while(i<=n):
    print( "*"*i + " "*space + "*"*i + " "*space + "*"*i + " "*space + "*"*i)
    space -= 1
    i += 1
