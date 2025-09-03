# https://www.geeksforgeeks.org/problems/check-for-subsequence4930/0


def isSubSequence(A, B):
    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            i += 1
        j += 1

    return i == len(A)


# def isSubSequence(A, B):
#     index = 0
#     output = str()
#     for char in A:
#         for i in range(index, len(B)):
#             if char == B[i]:
#                 index = i + 1
#                 output += char
#                 break

#     if output == A:
#         return True
#     else:
#         return False

print(isSubSequence(A="AXY", B="YADXCP"))
print(isSubSequence(A="gksrek", B="geeksforgeeks"))
