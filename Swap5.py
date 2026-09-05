print("Enter your String:")

str1 = input()
org_str = str1

rev = ""

length = len(str1)

for i in range(length - 1, -1, -1):
    rev = rev + str1[i]

if org_str == rev:
    print(org_str, "is Palindrome String")
else:
    print(org_str, "is Not Palindrome String")
