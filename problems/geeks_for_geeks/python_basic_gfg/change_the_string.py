# https://www.geeksforgeeks.org/problems/change-the-string3541/0
# Change the string case depending on the first char of the string
def check_case(s: str):
    if s[0] >= 'A' and s[0] <= 'Z':
        return 'upper'
    elif s[0] >= 'a' and s[0] <= 'z':
        return 'lower'

def modify(s: str):
    case_to_convert = check_case(s)
    output = str()
    for i in s:
        if i >= 'A' and i <= 'Z' and case_to_convert == 'upper':
            output += i
        elif i >= 'a' and i <= 'z' and case_to_convert == 'lower':
            output += i
        elif i >= 'A' and i <= 'Z' and case_to_convert == 'lower':
            output += chr(ord(i) + 32)
        elif i >= 'a' and i <= 'z' and case_to_convert == 'upper':
            output += chr(ord(i) - 32)

    return output

print(modify('aBCDEF'))
