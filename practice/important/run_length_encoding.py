# https://www.geeksforgeeks.org/problems/run-length-encoding/1


# def encode(s: str) -> str:
# output = str()
# count = [s[0], 0]
# index = 0

# for char in s:
#     if char == count[index]:
#         count[index + 1] += 1
#     else:
#         count.append(char)
#         count.append(1)
#         index += 2

# for value in count:
#     if type(value) is not str:
#         output += str(value)
#     else:
#         output += value

# return output


def encode(s: str) -> str:
    output = ""
    i = 0

    while i < len(s):
        output += s[i]
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        else:
            i += 1

        output += str(count)

    return output


print(encode("aaaabbbcccaaaaa"))
