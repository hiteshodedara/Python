#Python set..
print("Python Set...\n\n")

s = {'a', 'b', 'c', 'd', 'e', 'f'}
s2 = {'e', 'f', 'g', 'h', 'i', 'j'}
print("Our set is : ", sorted(s))

s.add('g')
print("Added 'g' : ", sorted(s))

s.discard('a')
print("Discard 'a' : ", sorted(s))

print("Merge s and s2 : ", sorted(s|s2))
print("Values in both s and s2 : ", sorted(s & s2))
print("s - s2 : ", sorted(s - s2))
