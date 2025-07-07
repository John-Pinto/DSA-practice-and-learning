# https://www.geeksforgeeks.org/problems/count-type-of-characters3635/0
def count(s):
    upper = 0
    lower = 0
    numeric = 0
    special = 0

    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            upper += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            lower += 1
        elif ord(char) >= 48 and ord(char) <= 57:
            numeric += 1
        else:
            special += 1

    return upper, lower, numeric, special


print(count("#GeeKs01fOr@gEEks07"))
