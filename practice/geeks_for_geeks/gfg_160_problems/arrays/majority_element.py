def find_majority(arr):
    n = len(arr)

    elem_1, elem_2 = -1, -1
    count_1, count_2 = 0, 0

    for elem in arr:
        # Increment count for first candidate
        if elem_1 == elem:
            count_1 += 1

        # Increment count for second candidate
        elif elem_2 == elem:
            count_2 += 1

        # Select the element as candidate if
        # count is 0 and increment the count
        elif count_1 == 0:
            elem_1 = elem
            count_1 += 1

        elif count_2 == 0:
            elem_2 = elem
            count_2 += 1

        # Decrease count if unknown element occurs
        else:
            count_1 -= 1
            count_2 -= 1

    # Updating count based on the final elements
    count_1, count_2 = 0, 0

    for elem in arr:
        if elem_1 == elem:
            count_1 += 1

        if elem_2 == elem:
            count_2 += 1

    # Checking if selected element have a count of more than n/3.
    output = []

    if count_1 > n / 3:
        output.append(elem_1)

    if count_2 > n / 3:
        output.append(elem_2)

    return sorted(output)


print(find_majority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))
print(find_majority([1, 2, 3, 4, 5]))
