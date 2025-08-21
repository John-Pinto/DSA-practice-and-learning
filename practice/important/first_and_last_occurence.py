# https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

# Using first binary search to get the target
# then using two pointer method to locate the lower and upper bound


def find(arr, x):
    low = 0
    high = len(arr) - 1
    first_index = -1

    while low <= high:
        mid = (high - low) // 2 + low

        if arr[mid] == x:
            first_index = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    low = 0
    high = len(arr) - 1
    last_index = -1

    while low <= high:
        mid = (high - low) // 2 + low

        if arr[mid] == x:
            last_index = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return [first_index, last_index]


print(find(arr=[5, 7, 7, 7, 8, 8, 8, 100], x=100))
print(find(arr=[1, 7, 7, 7, 8, 8, 8, 10], x=1))
print(find(arr=[5, 7, 7, 7, 8, 8, 8], x=8))
print(find(arr=[1, 3, 5, 5, 5, 5, 67, 123, 125], x=5))
print(find(arr=[1, 3, 5, 5, 5, 5, 7, 123, 125], x=7))
print(find(arr=[1, 2, 3], x=4))
