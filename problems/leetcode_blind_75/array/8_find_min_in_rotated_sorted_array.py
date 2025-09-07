# Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# def findMin(nums) -> int:
#     n = len(nums)
#     left = 0
#     right = n - 1
#     min_value = nums[0]

#     while left <= right:
#         mid = (right - left) // 2 + left
#         min_value = min(min_value, nums[mid])

#         if nums[mid] < nums[left] and nums[mid] < nums[right]:
#             right = mid - 1

#         elif nums[mid] > nums[left] and nums[mid] > nums[right]:
#             left = mid + 1

#         elif mid == left:
#             left += 1
#         else:
#             right -= 1

#     return min_value


def findMin(nums):
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        mid = (right - left) // 2 + left

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


print(findMin([1, 2, 3, 4, 5]))
print(findMin([5, 4, 1, 2, 3]))
print(findMin([2, 3, 4, 5, 1]))
print(findMin([5, 1, 4]))
print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([11, 13, 15, 17]))
