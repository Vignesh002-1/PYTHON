num = 12345

even_count = 0
odd_count = 0

while num > 0:
    rem = num % 10

    if rem % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    num = num // 10

print("Even Digits:", even_count)
print("Odd Digits:", odd_count)
