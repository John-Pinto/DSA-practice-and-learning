# https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1?page=1&category=Strings&difficulty=Basic&status=solved&sortBy=submissions

def getMaxOccurringChar(s):
    hash = [0] * 26

    for i in s:
        hash[ord(i) - ord("a")] += 1

    max_value = 0
    max_char = ""

    for j in range(len(hash)):
        if hash[j] > max_value:
            max_value = hash[j]
            max_char = chr(ord("a") + j)

    return max_char

print(getMaxOccurringChar("sampletext"))
print(getMaxOccurringChar("jtyiki"))
print(getMaxOccurringChar("pqrst"))
