# Majority Voting Algorithm: Searches for the majority element or candidate in an array.
# Depending on the majority condition, number of candidate changes:
# Consider n as size of array and k as majority occupancy in the array.
# So, 1. A 50% occupancy will have, n/2, here k is 2 and k - 1 is 1
# i.e. only one candidate with majority vote.
# 2. A 33% occupancy n/3, is 3 - 1 = 2, i.e. 2 candidates
# 3. A 25% occupancy n/4, is 4 - 1 = 3, i.e. 3 candidates and so on.

# Read article:
# 1. https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/
# 2. https://www.geeksforgeeks.org/dsa/majority-element/
# 3. https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote


def find_majority_one_third(arr):
    n = len(arr)

    # two candidates for finding n/3 majority
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


print(find_majority_one_third([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))
print(find_majority_one_third([1, 2, 3, 4, 5]))
