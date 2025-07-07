# https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?page=1&category=Arrays&difficulty=Easy&status=solved&sortBy=submissions


# def findTwoElement(arr):
#     arr.sort()
#     count = [0] * (len(arr) + 1)

#     for i in range(len(arr)):
#         count[arr[i]] += 1

#     missing = 0
#     repeat = 0

#     for i in range(len(count)):
#         if count[i] == 0:
#             missing = i
#         elif count[i] == 2:
#             repeat = i
#     return repeat, missing


# def findTwoElement(arr):
#     # code here
#     n = len(arr)
#     ans = [0] * 2

#     # Creating visited vector of size n+1 with
#     # initial values as false. Note that array
#     # values will go upto n, that is why we
#     # have taken the size as n+1
#     visited = [False] * (n + 1)
#     repeating = -1
#     missing = -1

#     for i in range(n):
#         if visited[arr[i]]:
#             repeating = arr[i]
#         else:
#             visited[arr[i]] = True

#     for i in range(1, n + 1):
#         if not visited[i]:
#             missing = i
#             break

#     ans[0] = repeating
#     ans[1] = missing

#     return ans


def findTwoElement(arr):
    temp_set = set()

    for i in arr:
        if i in temp_set:
            repeating = i
        else:
            temp_set.add(i)

    array_sum = sum(arr)

    actual_sum = (len(arr) * (len(arr) + 1)) // 2

    missing = actual_sum - (array_sum - repeating)

    return repeating, missing


print(findTwoElement([4, 3, 6, 2, 1, 1]))
