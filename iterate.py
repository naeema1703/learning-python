fruits = ["apple", "banana", "orange", "pineapple"]

for fruit in fruits:
    print(fruit.upper())

index = 0

while index < len(fruits):
      print(fruits[index].upper())
      index += 1

uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)