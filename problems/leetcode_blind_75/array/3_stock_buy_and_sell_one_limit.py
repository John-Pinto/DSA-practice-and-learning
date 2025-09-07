# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


def maximumProfit(prices):
    sell = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        buy = min(buy, prices[i])

        sell = max(sell, prices[i] - buy)

    return sell


print(maximumProfit([7, 10, 1, 3, 6, 9, 2]))
print(maximumProfit([7, 6, 4, 3, 1]))
print(maximumProfit([1, 3, 6, 9, 11]))
