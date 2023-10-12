# List
fruits = ["Apple", "Peach", "Pear"]

# for loop in list
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

# for loop in range
for number in range(1, 10):
  print(number)
  
# Carl Gauss  - German Mathematician
total = 0
for number in range(1, 101):
  total += number
print(total)

# Adding even numbers

target = int(input())

even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)
  