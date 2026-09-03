def reverse_using_concat(s):
    """1. Using + (string concatenation) operator"""
    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev = rev + s[i]
    print("Reverse String is:", rev)


def reverse_using_char_list(s):
    """2. Using a character list (like Java's char array)"""
    chars = list(s)
    rev = ""
    for i in range(len(chars) - 1, -1, -1):
        rev = rev + chars[i]
    print("Reverse String is:", rev)


def reverse_using_slicing(s):
    """3. Using Python slicing (Pythonic equivalent of StringBuffer.reverse())"""
    rev = s[::-1]
    print("Reverse String is:", rev)


if __name__ == "__main__":
    str_val = "ABCD"

    reverse_using_concat(str_val)
    reverse_using_char_list(str_val)
    reverse_using_slicing(str_val)
