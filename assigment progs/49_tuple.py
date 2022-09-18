print("Python Tuples...\n\n")

t1, t2 = (1,2,3,4,5,6,7,8,9), ('a', 'b', 'c', 'd','e','f','g','h','i')

print("t1[1:7] : " , str(t1[1:7]))
print("t2[:4] : " , str(t2[:4]))
print("Max value in t1 : ",max(t1))
print("Min value in t2 : ", min(t2))
print("Concatenation of two tuples : ", t1 + t2)
