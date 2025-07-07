# https://www.geeksforgeeks.org/problems/sum-of-series2811/0

def series_sum(n : int) -> int:
    if n == 1:
        return n
    else:
        return n + series_sum(n - 1)
    
print(series_sum(999))