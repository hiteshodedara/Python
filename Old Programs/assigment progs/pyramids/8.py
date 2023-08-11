n = int(input("Enter the number of lines : "))
space = n

print("\nfor loop...")
for i in range(n+1):
    print(" "*space,"*"*i)
    space-=1
space = 1
for i in range(n-1, 0, -1):
    print(" "*space,"*"*i)
    space+=1
    

i = 0
space = n
print("\nwhile loop..")
while(i<=n):
    print(" "*space,"*"*i)
    space-=1
    i += 1
space = 1
i = n-1
while(i>0):
    print(" "*space,"*"*i)
    space+=1
    i-=1
