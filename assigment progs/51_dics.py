#Python Dictionary...
print("\nPython Dictionary..\n")


dict = {'name' : 'Raj Solanki', 'mono' : '9313310090', 'email' : 'raj6solanki@gmail.com', 'game' : 'Cricket'}

print("Dict. : ", dict)
print("dict[name] : ", dict['name'])

print("Change value of game... ")
dict['game'] = 'Chess'
print("dict['game'] : ", dict['game'])

print("Delete email index form dict...")
del dict['email']
print("dict = ", dict)

print("Keys of dict : ", dict.keys())
print("Values of dict : ", dict.values())

print("Clearing the dict : ", dict.clear())
