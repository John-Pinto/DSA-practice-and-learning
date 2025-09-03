# https://www.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/0

def is_isogram(s):
        isogram_dict = {}
        
        for char in s:
            if char in isogram_dict:
                return False
            else:
                isogram_dict[char] = 1
            
        return True

# def is_isogram(self,s):
#         for i in range(len(s)):
#             char = s[i]
#             for j in range(i+1, len(s)):
#                 if char == s[j]:
#                     return False
        
#         return True


print(is_isogram('machine'))
print(is_isogram('geeks'))