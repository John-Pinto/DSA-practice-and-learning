# 3Sum
# https://leetcode.com/problems/3sum/description/


def threeSum(nums):
    output = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                output.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

    return output


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(threeSum(nums=[0, 1, 1]))
print(threeSum(nums=[0, 0, 0]))
