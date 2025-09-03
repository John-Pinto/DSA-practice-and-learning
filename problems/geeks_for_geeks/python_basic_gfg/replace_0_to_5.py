# https://www.geeksforgeeks.org/problems/replace-all-0s-with-5/0
def convert0to5rec(num):
    # Base case for recursion termination
    if num == 0:
        return 0

    # Extract the last digit and change it if needed
    digit = num % 10

    if digit == 0:
        digit = 5

    # Convert remaining digits and append the last digit
    return convert0to5rec(num // 10) * 10 + digit


# It handles 0 to 5 calls convert0to5rec()
# for other numbers
def convert0to5(num):
    if num == 0:
        return 5
    else:
        return convert0to5rec(num)


# Driver Program
num = 10120
print(convert0to5(num))
