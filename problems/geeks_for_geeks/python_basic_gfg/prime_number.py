# https://www.geeksforgeeks.org/problems/prime-number2314/1

import math


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


# def isPrime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n // 2):
#         if n % i == 0:
#             return False

#     return True


print(isPrime(13))
print(isPrime(25))
print(isPrime(173))
