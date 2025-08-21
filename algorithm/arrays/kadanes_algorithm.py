# Kadanes Algorithm: Calculating maximum sum of a subarray.
# For explanation:
# https://www.geeksforgeeks.org/dsa/print-the-maximum-subarray-sum/
# https://www.geeksforgeeks.org/dsa/maximum-product-subarray/
# https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-array-created-repeated-concatenation/
# https://www.youtube.com/watch?v=hLPkqd60-28


def kadanes_sum(arr: list):
    curr_sum = 0
    max_sum = float("-inf")

    for i in range(len(arr)):
        curr_sum += arr[i]

        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


def kadanes_subarray(arr: list):
    curr_sum = arr[0]
    max_sum = arr[0]

    curr_start = 0
    start = 0
    end = 0

    for i in range(1, len(arr)):
        if curr_sum + arr[i] < arr[i]:
            curr_sum = arr[i]
            curr_start = i
        else:
            curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

            start = curr_start
            end = i

    output = arr[start : end + 1]

    return output


print(
    "subarray: ",
    kadanes_subarray([2, 3, -8, 7, -1, 2, 3]),
    "sum: ",
    kadanes_sum([2, 3, -8, 7, -1, 2, 3]),
)

print(
    "subarray: ",
    kadanes_subarray([-2, -4]),
    "sum: ",
    kadanes_sum([-2, -4]),
)

print(
    "subarray: ",
    kadanes_subarray([5, 4, 1, 7, 8]),
    "sum: ",
    kadanes_sum([5, 4, 1, 7, 8]),
)
