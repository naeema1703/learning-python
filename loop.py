numbers = []

user_input = input("enter a number or type stop: ")

while user_input != "stop":

  numbers.append(int(user_input))

  user_input = input("enter a number or type stop: ")


for number in numbers:
    if number % 2 == 0:
        print(number)










    