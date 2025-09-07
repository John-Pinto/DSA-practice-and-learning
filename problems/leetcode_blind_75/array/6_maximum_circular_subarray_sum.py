# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620

# Using the formula "circular_sum = total_sum - normal_min",
# normal max and min are found using the kadane algorithm.
def circular_subarray_sum(arr):
    curr_max = 0
    curr_min = 0

    max_sum = arr[0]
    min_sum = arr[0]

    total_sum = 0

    for i in range(len(arr)):
        # finding maximum sum
        curr_max = max(curr_max + arr[i], arr[i])
        max_sum = max(max_sum, curr_max)

        # finding minimum sum
        curr_min = min(curr_min + arr[i], arr[i])
        min_sum = min(min_sum, curr_min)

        total_sum += arr[i]

    circular_sum = total_sum - min_sum

    if total_sum == min_sum:
        return max_sum

    return max(max_sum, circular_sum)


print(circular_subarray_sum([8, -8, 9, -9, 10, -11, 12]))
print(circular_subarray_sum([10, -3, -4, 7, 6, 5, -4, -1]))
print(circular_subarray_sum([-1, 40, -14, 7, 6, 5, -4, -1]))
