# https://www.geeksforgeeks.org/problems/repeated-character2058/0


def firstRep(s):
    # Creating an empty dictionary to store the frequency of each character
    count_dict = {}

    # iterating over the string
    for i in s:
        # checking if the character is already present in the dictionary
        if i in count_dict:
            # if yes, increment its frequency by 1
            count_dict[i] += 1
        else:
            # if not, add the character to the dictionary with frequency 1
            count_dict[i] = 1

    # iterating over the string again
    for i in s:
        # checking if the frequency of the character is greater than 1
        if count_dict[i] > 1:
            # if yes, return the character
            return i

    # if no repeated characters found, return -1
    return -1


# def firstRep(self, s):
#     for i in range(len(s)):
#         char = s[i]
#         for j in range(i + 1, len(s)):
#             if char == s[j]:
#                 return char

#     return "#"


print(firstRep(s="geeksforgeeks"))
print(firstRep(s="abcde"))
