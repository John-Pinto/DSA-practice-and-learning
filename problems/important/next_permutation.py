# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/next-permutation5226


def next_permutation(arr: list):
    n = len(arr)

    pivot = -1

    # Finding pivot index that is smaller than its index + 1 neighbour
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # If pivot does not exist
    # then the array is the max permutation
    # so reversing the array to the initial permutation
    if pivot == -1:
        arr.reverse()
        return arr

    # if pivot exist then swaping place with the max element
    for i in range(n - 1, -1, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reversing all the elements from the pivot
    start = pivot + 1
    end = n - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


print(next_permutation([2, 4, 1, 7, 5, 0]))
print(next_permutation([3, 2, 1]))
print(next_permutation([3, 4, 2, 5, 1]))
