# https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1


# def isBalanced(s):
#     stack = []

#     open_brackets = "[{("

#     for char in s:
#         if char in open_brackets:
#             stack.append(char)
#         else:
#             if stack:
#                 open = stack.pop()
#             else:
#                 return False

#             if char == "]":
#                 if open == "[":
#                     continue
#                 else:
#                     return False
#             elif char == "}":
#                 if open == "{":
#                     continue
#                 else:
#                     return False
#             elif char == ")":
#                 if open == "(":
#                     continue
#                 else:
#                     return False

#     if stack:
#         return False
#     else:
#         return True


def isBalanced(s):
    stack = []

    open_brackets = "[{("

    for char in s:
        if char in open_brackets:
            stack.append(char)
        else:
            if stack and (
                (stack[-1] == "(" and char == ")")
                or (stack[-1] == "[" and char == "]")
                or (stack[-1] == "{" and char == "}")
            ):
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True


print(isBalanced("[{()}]"))
print(isBalanced("[()()]{}"))
print(isBalanced("([]"))
print(isBalanced("([{]})"))
