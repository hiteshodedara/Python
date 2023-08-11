n = int(input("Enter the number for create diamand : "))

start = n
en = int(0)
i = int(1)

#for loop..
print("\nfor loop...")
for space in range(start, en, -1):
    print(" "*space, "*"*i)
    i+=2
for space in range(0, start+1):
    print(" "*space, "*"*i)
    i-=2


#while loop...
print("\nWhile loop...")
i = int(1)
space = n

while(space > 0):
    print(" "*space, "*"*i)
    i+=2
    space -= 1
while(space <= n):
    print(" "*space, "*"*i)
    i-=2
    space += 1
