# https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1?page=1&category=Strings&difficulty=Easy&status=solved&sortBy=submissions


# def areRotations(s1, s2):
#     for i in range(len(s1)):
#         if s1[i] == s2[0]:
#             output = s1[i:] + s1[:i]
#             if output == s2:
#                 return True

#     return False


def areRotations(s1, s2):
    if len(s1) == len(s2) and s2 in s1 + s1:
        return True
    return False


print(areRotations(s1="abcd", s2="cdab"))
print(areRotations(s1="aab", s2="aba"))
print(areRotations(s1="abcd", s2="acbd"))
