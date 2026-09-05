print("Enter a number:")

num = int(input())

org_num = num
rev = 0

while num != 0:
    rev = rev * 10 + num % 10
    num = num // 10

if org_num == rev:
    print(org_num, "Palindrome Number")
else:
    print(org_num, "Not Palindrome Number")
