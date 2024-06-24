# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers2)

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])



print("# Get length")
print(len(fruits))

print("# Append to list")
fruits.append('Mangos')
print(fruits)

print("# Remove from list")
fruits.remove('Grapes')
print(fruits)

print("#Insert into position")
fruits.insert(2, 'Strawberries')
print(fruits)

print("#change values using index")
fruits[0] = 'Blueberries'
print(fruits)

print("# Remove with pop")
fruits.pop(2)
print(fruits)

print("# Reverse list using reverse() method")
fruits.reverse()
print(fruits)

print("# Sort list")
fruits.sort()
print(fruits)

print("# Reverse sort")
fruits.sort(reverse=True)


print(fruits)
