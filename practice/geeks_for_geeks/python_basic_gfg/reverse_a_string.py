# https://www.geeksforgeeks.org/problems/java-reverse-a-string0416/0


def revStr(s: str) -> str:
    i_pointer = 0
    j_pointer = len(s) - 1

    output = [0] * len(s)

    while i_pointer <= j_pointer:
        output[i_pointer], output[j_pointer] = s[j_pointer], s[i_pointer]
        i_pointer += 1
        j_pointer -= 1

    return "".join(output)


# def revStr(self, s: str) -> str:
#     output = str()
#     for i in range(len(s) - 1, -1, -1):
#         output += s[i]

#     return output


print(revStr("GeeksforGeeks"))
print(revStr("ReversE"))
print(revStr("Custom"))
