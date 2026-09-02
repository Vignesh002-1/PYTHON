class Swapping2Numbers:

    def main(self):

        a = 10
        b = 20

        print("Before swapping values are..", a, b)

        # Logic 1 - Using third variable
        # t = a
        # a = b
        # b = t

        # Logic 2 - Using + and -
        # a = a + b
        # b = a - b
        # a = a - b

        # Logic 3 - Using * and /
        # a and b should not be zero
        # a = a * b
        # b = a // b
        # a = a // b

        # Logic 4 - Using Bitwise XOR
        # a = a ^ b
        # b = a ^ b
        # a = a ^ b

        # Single statement
        a, b = b, a

        print("After swapping values are..", a, b)


obj = Swapping2Numbers()
obj.main()
