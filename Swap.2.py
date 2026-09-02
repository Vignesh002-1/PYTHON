class ReverseNumber:

    def main(self):

        num = int(input("Enter a Number: "))

        # 1. Using Algorithm
        rev = 0
        temp = num

        while temp != 0:
            rev = rev * 10 + temp % 10
            temp = temp // 10

        print("Reverse Number is:", rev)

        # 2. Using StringBuffer equivalent
        sb = str(num)
        rev = sb[::-1]

        print("Reverse Number using String:", rev)

        # 3. Using StringBuilder equivalent
        sb1 = ""
        sb1 = sb1 + str(num)

        print("StringBuilder value:", sb1)


obj = ReverseNumber()
obj.main()
