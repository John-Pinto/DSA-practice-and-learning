# https://leetcode.com/problems/contains-duplicate


def containsDuplicate(nums):
    store = set()
    for i in nums:
        if i in store:
            return True
        else:
            store.add(i)

    return False


print(containsDuplicate(nums=[1, 2, 3, 1]))
print(containsDuplicate(nums=[1, 2, 3, 4]))
print(containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
