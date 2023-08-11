n = int(input("Enter number of the lines : "))

start = n
en = int(0)


#for loop
print("\nfor loop...")
for i in range(start,en, -1):
    print("*"*i)


#while loop..
i = n
print("\nwhile loop...")
while (i>0):
    print("*"*i)
    i-=1
