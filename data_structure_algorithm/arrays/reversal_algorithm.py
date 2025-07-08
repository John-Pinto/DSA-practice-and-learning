# Reversal Algorithm: Rotating 1-D array in either direction.
# For explanation read: https://www.geeksforgeeks.org/dsa/complete-guide-on-array-rotations/ and https://www.geeksforgeeks.org/dsa/array-rotation/


def reversal(array: list, start: int, end: int) -> list:
    while start < end:
        # Swap all the values between start and end
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array


def left_rotation(array: list, d: int) -> list:
    # Calculating the d value if it is greater than length of array
    print(f"Rotating array anti-clockwise (left rotation): {array} for {d} rotation.")
    n = len(array)
    d %= n

    # Initial reversal of first d elements
    array = reversal(array=array, start=0, end=d - 1)

    # Next, reversal of the remaining elements
    array = reversal(array=array, start=d, end=n - 1)

    # Lastly, reversal of the whole array
    array = reversal(array=array, start=0, end=n - 1)

    print(f"After applying {d} rotation, resultant array: {array}.\n")

    return array


def right_rotation(array: list, d: int) -> list:
    # Calculating the d value if it is greater than length of array
    print(f"Rotating array clockwise (right rotation): {array} for {d} rotation.")
    n = len(array)
    d %= n

    # Initial reversal of first d elements
    array = reversal(array=array, start=n - d, end=n - 1)

    # Next, reversal of the remaining elements
    array = reversal(array=array, start=0, end=(n - d) - 1)

    # Lastly, reversal of the whole array
    array = reversal(array=array, start=0, end=n - 1)

    print(f"After applying {d} rotation, resultant array: {array}.\n")

    return array


if __name__ == "__main__":
    right_rotation(array=[1, 2, 3, 4, 5], d=2)
    left_rotation(array=[1, 2, 3, 4, 5], d=2)

    right_rotation(array=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d=3)
    left_rotation(array=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d=3)

    right_rotation(array=[7, 3, 9, 1], d=9)
    left_rotation(array=[7, 3, 9, 1], d=9)
