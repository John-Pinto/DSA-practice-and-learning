# https://www.geeksforgeeks.org/problems/second-largest3735/1?page=1&category=Arrays&sortBy=submissions

# def getSecondLargest(arr):
#     first_max = 0
#     second_max = -1

#     for i in arr:
#         if i >= first_max:
#             first_max = i

#     for j in arr:
#         if j >= second_max and j < first_max:
#             second_max = j

#     return second_max


def getSecondLargest(arr):
    first_max = -1
    second_max = -1

    for i in arr:
        if i > first_max:
            second_max = first_max
            first_max = i
        elif i > second_max and i < first_max:
            second_max = i

    return second_max


print(getSecondLargest(arr=[28078, 19451, 935, 28892, 2242, 3570, 5480, 231]))
print(getSecondLargest(arr=[12, 35, 1, 10, 34, 1]))
print(getSecondLargest(arr=[10, 5, 10]))
print(getSecondLargest(arr=[10, 10, 10]))
