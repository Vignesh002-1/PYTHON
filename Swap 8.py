num = 1234

sum = 0

while num > 0:
    sum = sum + num % 10
    num = num // 10

print("Sum of digits in a number:", sum)
