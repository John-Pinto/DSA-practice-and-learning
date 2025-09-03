# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604


# Min Max Approach: Here min and max are calculated together
# on every index and the max value is only stored
# def max_product(arr):
#     curr_max = arr[0]
#     curr_min = arr[0]
#     max_prod = arr[0]

#     for i in range(1, len(arr)):
#         temp = max(arr[i], arr[i] * curr_max, arr[i] * curr_min)

#         curr_min = min(arr[i], arr[i] * curr_max, arr[i] * curr_min)

#         curr_max = temp

#         max_prod = max(max_prod, curr_max)

#     return max_prod


# Traversing both direction approach: Here two pointers move
# simultaneously in opposite direction.
def max_product(arr):
    n = len(arr)

    max_prod = float("-inf")

    left_to_right = 1
    right_to_left = 1

    for i in range(n):
        if left_to_right == 0:
            left_to_right = 1
        if right_to_left == 0:
            right_to_left = 1

        left_to_right *= arr[i]

        j = (n - i) - 1
        right_to_left *= arr[j]

        max_prod = max(left_to_right, right_to_left, max_prod)

    return max_prod


print(max_product([-2, 6, -3, -10, 0, 2]))
print(max_product([-1, -3, -10, 0, 6]))
print(max_product([2, 3, 4]))
