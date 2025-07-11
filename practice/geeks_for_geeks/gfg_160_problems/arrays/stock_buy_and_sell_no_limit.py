# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615


# Approach - Local Minima and Maxima

# def maximum_profit(prices):
#     output = 0
#     n = len(prices)
#     l_min = prices[0]  # local minima
#     l_max = prices[0]  # local maxima

#     i = 0
#     while i < n - 1:
#         # Finding local minima
#         while i < n - 1 and prices[i] >= prices[i + 1]:
#             i += 1
#         l_min = prices[i]

#         # Finding local maxima
#         while i < n - 1 and prices[i] <= prices[i + 1]:
#             i += 1
#         l_max = prices[i]

#         output += l_max - l_min

#     return output


# Approach - Accumulate Profit


def maximum_profit(prices):
    output = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            output += prices[i] - prices[i - 1]

    return output


print(maximum_profit([100, 180, 260, 310, 40, 535, 695]))
print(maximum_profit([4, 2, 2, 2, 4]))
print(maximum_profit([100, 180, 260, 310, 40, 50, 20]))
