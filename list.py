#even_numbers = [number for number in range(1, 51) if number % 2 == 0]

#squares = [number ** 2 for number in even_numbers if number ** 2 > 200]

#print(even_numbers)
#print(squares)

squares = [1, 5, 6, 5]

sum = 0

for num in squares:
    sum += num
    print(sum)

#for i in range(100):
    #print(i)    
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
while i < len(a):
    print(a[i])
    i = i + 3
