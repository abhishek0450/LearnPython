# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
  print(f'Current Person: {person}')

print("# break if person == Sara")
for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

print("# Continue if person == Sara")
for person in people:
  if person == 'Sara':
    continue 
  print(f'Current Person: {person}')

# range
for i in range(len(people)):
  print(people[i])

for i in range(0, 11,2):
  print(f'Number: {i}')
  #stop
  #start stop
  #start stop step

# While loops execute a set of statements as long as a condition is true.

count = 1
while count <= 10:
  print(f'Count: {count}')
  count += 1


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\nloop on String")
for char in "hello":
    print(char)

print("\nloop on Dictionary")
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 92}
for student in student_scores:
    print(student)

print("\n")
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n loop on matrix")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)
