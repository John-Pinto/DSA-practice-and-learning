# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751


# def pushZerosToEnd(arr):
#     zero_count = 0
#     i = 0

#     while i < len(arr):
#         if arr[i] == 0:
#             zero_count += 1
#             i += 1
#         elif arr[i - 1] == 0:
#             arr[i], arr[i - zero_count] = arr[i - zero_count], arr[i]
#             i += 1
#         else:
#             i += 1

#     return arr


def pushZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

    return arr


print(pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))
print(pushZerosToEnd([10, 20, 30]))
print(pushZerosToEnd([0, 0]))
