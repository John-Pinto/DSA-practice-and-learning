# https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1

def minDist(arr, x, y):
    x_pos = -1
    y_pos = -1
    output = float("inf")

    for i in range(len(arr)):
        if arr[i] == x:
            x_pos = i
            if y_pos != -1:
                output = min(output, abs(x_pos - y_pos))
        elif arr[i] == y:
            y_pos = i
            if x_pos != -1:
                output = min(output, abs(y_pos - x_pos))

    if output == float("inf"):
        return -1
    else:
        return output


print(minDist(arr=[1, 2, 3, 2], x=2, y=1))
print(minDist(arr=[1, 2, 3, 2], x=1, y=2))
print(minDist(arr=[86, 39, 90, 67, 84, 66, 62], x=42, y=12))
print(minDist(arr=[10, 20, 30, 40, 50], x=10, y=50))
print(minDist(arr=[0, 2, 10, 9, 8, 7, 1, 3, 2, 2], x=1, y=2))
