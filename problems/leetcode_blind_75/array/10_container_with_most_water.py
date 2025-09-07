# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description


def maxArea(height):
    max_area = 0
    curr_area = 0

    left = 0
    right = len(height) - 1

    while left < right:
        if height[left] < height[right]:
            curr_area = (right - left) * height[left]
            left += 1

        else:
            curr_area = (right - left) * height[right]
            right -= 1

        max_area = max(max_area, curr_area)

    return max_area


print(maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea(height=[1, 1]))
print(maxArea(height=[19, 8, 17, 6, 15, 4, 3, 20]))
