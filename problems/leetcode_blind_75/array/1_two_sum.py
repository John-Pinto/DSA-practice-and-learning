# Two Sum
# https://leetcode.com/problems/two-sum/description


def twoSum(nums, target):
    output = {}

    for i, num in enumerate(nums):
        if num in output:
            return [output[num], i]
        else:
            output[target - num] = i


print(twoSum(nums=[2, 7, 11, 15], target=9))
print(twoSum(nums=[3, 2, 4], target=6))
print(twoSum(nums=[3, 3], target=6))
