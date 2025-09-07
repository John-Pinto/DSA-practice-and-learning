# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


def search(nums, target) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right - left) // 2 + left

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(search(nums=[4, 5, 6, 7, 1, 2, 3], target=5))
print(search(nums=[4, 5, 6, 7, 1, 2, 3], target=2))
print(search(nums=[7, 1, 2, 3, 4, 5, 6], target=5))
print(search(nums=[7, 1, 2, 3, 4, 5, 6], target=1))
print(search(nums=[1, 2, 3, 4, 5, 6, 7], target=6))
print(search(nums=[1, 2, 3, 4, 5, 6, 7], target=2))
print(search(nums=[4, 5], target=5))
print(search(nums=[4, 5], target=4))
print(search(nums=[1, 2, 3], target=3))
print(search(nums=[1, 2, 3], target=1))
print(search(nums=[1], target=0))
