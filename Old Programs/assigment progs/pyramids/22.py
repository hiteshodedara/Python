n = int(input("Enter the number of lines : "))

i = n*2+1

#for loop..
print("\nfor loop...")
for space in range(n+1):
    print(" "*space, "*"*i)
    i-=2
i += 4
for space in range(n-1, -1, -1):
    print(" "*space, "*"*i)
    i+=2


#while loop...
print("\nWhile loop...")
i = (n*2)+1
space = int(0)

while(space <= n):
    print(" "*space, "*"*i)
    i-=2
    space += 1
i += 4
space = n-1
while(space > -1):
    print(" "*space, "*"*i)
    i+=2
    space -= 1
