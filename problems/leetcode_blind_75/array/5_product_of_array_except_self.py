# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/


# def productExceptSelf(nums):
#     total_product = 1
#     zero_count = 0

#     for i in nums:
#         if i != 0:
#             total_product *= i
#         else:
#             zero_count += 1

#     if zero_count > 1:
#         return [0] * len(nums)

#     if zero_count == 1:
#         return [0 if i != 0 else total_product for i in nums]
#     else:
#         return [total_product // i for i in nums]


# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
def productExceptSelf(nums):
    output = len(nums) * [1]

    # Creating a prefix, here first the output is updated with left then left is been updated with
    # original value. This helps in left to carry forward the element in next loop.
    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]

    # Creating a suffix, similar to prefix just in reverse order.
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output


print(productExceptSelf(nums=[1, 2, 3, 4]))
print(productExceptSelf(nums=[-1, 1, 0, -3, 3]))
print(productExceptSelf(nums=[-1, 1, 0, -3, 3, 0]))
