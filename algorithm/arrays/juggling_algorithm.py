# Juggling Algorithm: Rotating 1-D array in either direction.
# For explanation read: https://www.geeksforgeeks.org/dsa/complete-guide-on-array-rotations/ and https://www.geeksforgeeks.org/dsa/array-rotation/

import math


def left_juggling(array: list, d: int) -> list:
    print(f"Rotating array anti-clockwise (left rotation): {array} for {d} rotation.")
    n = len(array)

    # Calculating no. of rotation in respect to length of array if d > n
    d %= n

    # Calculating greatest common divisor (gcd) for total cycles
    cycles = math.gcd(n, d)

    for i in range(cycles):
        curr_idx = i
        curr_elem = array[i]

        while True:
            next_idx = (curr_idx + d) % n

            if next_idx == i:
                break

            # Moving the right elements to left side direction.
            array[curr_idx] = array[next_idx]
            curr_idx = next_idx

        array[curr_idx] = curr_elem

    print(f"After applying {d} rotation, resultant array: {array}.\n")

    return array


def right_juggling(array: list, d: int) -> list:
    print(f"Rotating array clockwise (right rotation): {array} for {d} rotation.")
    n = len(array)

    # Calculating no. of rotation in respect to length of array if d > n
    d %= n

    # Calculating greatest common divisor (gcd) for total cycles
    cycles = math.gcd(n, d)

    for i in range(cycles):
        curr_idx = i
        curr_elem = array[i]

        while True:
            next_idx = (curr_idx + d) % n
            # Storing next element temporarily
            next_elem = array[next_idx]

            # Moving the left elements to right side direction.
            array[next_idx] = curr_elem

            # Updating current element with the previous next element
            curr_elem = next_elem

            curr_idx = next_idx

            if curr_idx == i:
                break

    print(f"After applying {d} rotation, resultant array: {array}.\n")

    return array


if __name__ == "__main__":
    right_juggling(array=[1, 2, 3, 4, 5], d=2)
    left_juggling(array=[1, 2, 3, 4, 5], d=2)

    right_juggling(array=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d=3)
    left_juggling(array=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d=3)

    right_juggling(array=[7, 3, 9, 1], d=9)
    left_juggling(array=[7, 3, 9, 1], d=9)
