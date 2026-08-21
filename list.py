even_numbers = [number for number in range(1, 51) if number % 2 == 0]

squares = [number ** 2 for number in even_numbers if number ** 2 > 200]

print(even_numbers)
print(squares)