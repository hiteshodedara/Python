print("Python list....\n\n")
list = [1,2,3,4,5,6]
list2 = ["A", "B", "C"]
print("This is our list : " + str(list))

print("list[4] : " + str(list[4])) #it prints the 4th index value from list.
print("list[2:5] : " + str(list[2:5])) #it prints list items from 2nd to 5th.
print("list[1:] : " + str(list[1:])) #it prints the list items from 1st to the last.
print("list[:3] : " + str(list[:3]))  #it prints the list items from 0 index to 3rd item.

list.append(7)  #append() add a item (7) in the list.
print("appended list : " + str(list))

list.remove(7) #remove() remove the item from the list.
print("Updated list : " + str(list))

print("index of value 5 : " + str(list.index(5)))  #index() returns the index of the given value in the list.

list.insert(3, 6)  #insert() change the value (6) at the index (3) in the list.
print("inserted 6 in index 3 : " + str(list))

print("how many times 6 occurs in list : " + str(list.count(6))) #count() count the given value occurance in the list.

list.extend(list2)  #it will marge two lists..
print("Extend two lists : " + str(list))
