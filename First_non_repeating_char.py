#Problem: Given a string, return the first character that appears exactly once.
#If every character repeats, return None.
s = "swiss"
def no_repeat(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char
    return None