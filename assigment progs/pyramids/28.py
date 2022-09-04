# Print Pascal's Triangle in Python
from math import factorial

# input n
n = int(input("Enter the number of lines : "))

#for loop...
print("\nFor loop...")
for i in range(n):
	for j in range(n-i+1):
		# for left spacing
		print(end=" ")
	for k in range(i+1):
		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(k)*factorial(i-k)), end=" ")
	# for new line
	print()


print("\nWhile loop...")
i = int(0)
while(i<n):
    j = int(0)
    k = int(0)
    while(j < n-i+1):
        print(end=" ")
        j += 1
    while(k<i+1):
        print(factorial(i)//(factorial(k)*factorial(i-k)), end=" ")
        k += 1
    i += 1
    print()
