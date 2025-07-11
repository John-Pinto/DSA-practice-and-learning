# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351


def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()

    output = arr[n - 1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - k < 0:
            continue

        min_height = min(arr[0] + k, arr[i] - k)

        max_height = max(arr[n - 1] - k, arr[i - 1] + k)

        output = min(output, max_height - min_height)

    return output


print(getMinDiff([12, 6, 4, 15, 17, 10], k=6))
print(getMinDiff([1, 5, 10, 15], k=3))
print(getMinDiff([1, 5, 8, 10], k=2))
print(getMinDiff([3, 9, 12, 16, 20], k=3))
