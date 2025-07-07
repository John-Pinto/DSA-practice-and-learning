# https://www.geeksforgeeks.org/problems/upper-case-conversion5419/0


def convert(s):
    flag = True
    output = str()
    for i in s:
        if flag and ord(i) >= 97 and ord(i) <= 122:
            flag = False
            output += chr(ord(i) - 32)
        elif ord(i) == 32:
            flag = True
            output += i
        else:
            output += i

    return output


print(convert("i love programming"))
