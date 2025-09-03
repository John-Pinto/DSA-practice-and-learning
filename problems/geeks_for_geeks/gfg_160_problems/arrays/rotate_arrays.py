# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621

import math

# Using juggling algorithm

# def rotateArr(arr, d):
#     n = len(arr)

#     d %= n

#     cycle = math.gcd(d, n)

#     for i in range(cycle):
#         curr_elem = arr[i]
#         curr_idx = i

#         while True:
#             next_idx = (curr_idx + d) % n
#             if next_idx == i:
#                 break

#             arr[curr_idx] = arr[next_idx]
#             curr_idx = next_idx

#         arr[curr_idx] = curr_elem

#     return arr

# Using reversal algorithm


def rotateArr(arr, d):
    n = len(arr)
    d %= n

    arr = reversal(arr=arr, start=0, end=d - 1)

    arr = reversal(arr=arr, start=d, end=n - 1)

    arr = reversal(arr=arr, start=0, end=n - 1)

    return arr


def reversal(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


print(rotateArr(arr=[1, 2, 3, 4, 5], d=2))
print(rotateArr(arr=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d=3))
print(rotateArr(arr=[7, 3, 9, 1], d=9))
