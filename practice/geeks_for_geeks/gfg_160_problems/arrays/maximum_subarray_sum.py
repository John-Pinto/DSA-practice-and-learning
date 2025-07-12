# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620


def max_subarray_sum(arr):
    curr_sum = 0
    max_sum = float("-inf")

    for i in range(len(arr)):
        curr_sum += arr[i]

        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


print(max_subarray_sum([2, 3, -8, 7, -1, 2, 3]))
print(max_subarray_sum([-2, -4]))
print(max_subarray_sum([5, 4, 1, 7, 8]))
