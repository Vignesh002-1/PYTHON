print("Enter First Number:")
a = int(input())

print("Enter Second Number:")
b = int(input())

print("Enter Third Number:")
c = int(input())

# Approach 1 - Logic

if a > b and a > c:
    print(a, "is Largest Number")
elif b > a and b > c:
    print(b, "is Largest Number")
else:
    print(c, "is Largest Number")


# Approach 2 - Ternary Operator

largest = a if a > b and a > c else (b if b > c else c)

print(largest, "is Largest Number (Ternary Operator)")
