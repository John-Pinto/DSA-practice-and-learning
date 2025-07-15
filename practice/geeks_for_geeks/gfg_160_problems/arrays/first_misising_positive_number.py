# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/smallest-positive-missing-number-1587115621

# Approach: Cycle sort algorithm
def missing_number(arr):
    n = len(arr)

    for i in range(n):
        # elements should be within the range and
        # should be at the same index (1 - indexing)
        # if not then swap it
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    # Finding the missing element that does not match with the index
    for i in range(1, n + 1):
        if i != arr[i - 1]:
            return i

    return n + 1

print(missing_number([2, 2, -5, 2, -2, 7, 1, -8]))
print(missing_number([2, -3, 4, 1, 1, 7]))
print(missing_number([5, 3, 2, 5, 1]))
print(missing_number([-8, 0, -1, -4, -3]))
