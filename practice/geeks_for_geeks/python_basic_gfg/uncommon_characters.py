# https://www.geeksforgeeks.org/problems/uncommon-characters4932/0


def uncommonChars(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    s1_hash = [0] * 26
    s2_hash = [0] * 26

    for i in s1:
        s1_hash[ord(i) - ord("a")] = 1

    for i in s2:
        s2_hash[ord(i) - ord("a")] = 1

    output = ""

    for i in range(len(s1_hash)):
        if s1_hash[i] > 0 and s2_hash[i] == 0:
            output += chr(ord("a") + i)
        elif s2_hash[i] > 0 and s1_hash[i] == 0:
            output += chr(ord("a") + i)

    return output


print(uncommonChars(s1="geeksforgeeks", s2="geeksquiz"))
print(uncommonChars(s1="characters", s2="alphabets"))
print(uncommonChars(s1="rome", s2="more"))
